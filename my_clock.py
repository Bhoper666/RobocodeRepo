from datetime import datetime

time_hour = datetime.now().strftime('%H')
time_minutes = datetime.now().strftime('%M')
date_year = datetime.now().strftime('%Y')
date_month = datetime.now().strftime('%m')
date_day = datetime.now().strftime('%d')

print(f'Time now: {time_hour}:{time_minutes} Date now: {date_year}|{date_month}|{date_day}')
