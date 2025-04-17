import threading
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authorize_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("ThreadTestSheet").worksheet("Sheet1")  # Change names if needed
    return sheet



class DataSender(threading.Thread):
    def __init__(self, sheet):
        threading.Thread.__init__(self)
        self.sheet = sheet
        self.running = True

    def run(self):
        counter = 0
        while self.running:
            counter += 1
            self.sheet.update(range_name='A3', values=[[f'Something is happening {counter}']])

            print(f"[Sender] Wrote: Message {counter}")
            time.sleep(3)

    def stop(self):
        self.running = False



class DataMonitor(threading.Thread):
    def __init__(self, sheet, sender_thread):
        threading.Thread.__init__(self)
        self.sheet = sheet
        self.sender_thread = sender_thread

    def run(self):
        while True:
            value = self.sheet.acell('A5').value
            print(f"[Monitor] Read A5: {value}")
            if value == '1':
                print("[Monitor] Restarting Thread 1...")
                self.sender_thread.stop()
                self.sender_thread.join()
                # Clear A5 to avoid infinite loop
                self.sheet.update('A5', '1')
                # Restart thread 1
                self.sender_thread = DataSender(self.sheet)
                self.sender_thread.start()
            time.sleep(5)


def main():
    sheet = authorize_sheets()
    sender = DataSender(sheet)
    monitor = DataMonitor(sheet, sender)
    sender.start()
    monitor.start()

if __name__ == '__main__':
    main()
