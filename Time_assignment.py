from datetime import datetime, date
while True:
    try:
        x = input("Please enter start date and time, use the format DD/MM/YY HH:MM:")
        start_date = datetime.strptime(x,"%d/%m/%y %H:%M") 
        break
    except ValueError as e:
        print('Please use the format DD/MM/YY HH:MM:')
print(start_date)


while True:
    try:
        x = input("Please enter end date and time, use the format DD/MM/YY HH:MM:")
        end_date = datetime.strptime(x,"%d/%m/%y %H:%M") 
        break
    except ValueError as e:
        print('Please use the format DD/MM/YY HH:MM:')
print(end_date)


total_seconds=work_time.seconds
    #print('tot sec: ', total_seconds)
hours = total_seconds/3600
    #print('tot hours: ', hours)
hours_days = work_time.days
    #print('tot hoursdays: ', hours_days)
total_hours = hours + (hours_days * 24)
    #print('tot_hours: ', total_hours)
rate_of_pay = 5
total_pay = round(total_hours * rate_of_pay, 2)
print(f'Your total pay is {currency}', total_pay)
today = date.today()