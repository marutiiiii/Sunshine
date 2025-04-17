#include <stdio.h>

int main() {
    float start_hour, end_hour, break_time;
    float daily_hours, total_hours = 0;
    int days = 0;
    char choice;

    printf("Work Hour Calculator\n");
    printf("-------------------\n");

    do {
        days++;
        printf("\nDay %d\n", days);

        
        printf("Enter start time (e.g., 9.5 for 9:30): ");
        scanf("%f", &start_hour);

        
        printf("Enter end time (e.g., 17.5 for 5:30 PM): ");
        scanf("%f", &end_hour);

       
        printf("Enter break time in hours (e.g., 0.5 for 30 mins): ");
        scanf("%f", &break_time);

        
        daily_hours = end_hour - start_hour - break_time;
        total_hours += daily_hours;

        printf("Today's work hours: %.2f hours\n", daily_hours);

        
        printf("\nAdd another day? (y/n): ");
        scanf(" %c", &choice); 
        
    } while (choice == 'y' || choice == 'Y');

    
    printf("\nSummary\n");
    printf("Total days worked: %d\n", days);
    printf("Total work hours: %.2f hours\n", total_hours);
    printf("Average per day: %.2f hours\n", total_hours/days);

    return 0;
}