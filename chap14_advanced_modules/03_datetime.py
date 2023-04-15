import datetime

time = datetime.time(2, 30)
print(f'Time\t\t\t\t\t\t\t\t\t\t: {time}')

date = datetime.date(1990, 1, 1)
print(f'Date\t\t\t\t\t\t\t\t\t\t: {date}')
print(f'Date fomrated\t\t\t\t\t\t\t\t\t: {date.ctime()}')
today = datetime.date.today()
print(f'Today\t\t\t\t\t\t\t\t\t\t: {today}')


daytime = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(f'Datetime\t\t\t\t\t\t\t\t\t: {daytime}')
new_daytime = daytime.replace(year=2022)
print(f'Datetime with year replced\t\t\t\t\t\t\t: {new_daytime}')
print(f'Original datetime unchanged\t\t\t\t\t\t\t: {daytime}')

date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2022, 11, 3)
difference = date2 - date1
print(
    f'Day difference between date {date1} and {date2}\t\t\t\t: {difference.days}')

datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2022, 11, 3, 12, 0)
difference = datetime2 - datetime1
print(
    f'Seconds difference between datetime {datetime1} and {datetime2}\t: {difference.seconds}')

time1 = datetime.time(2, 0)
time2 = datetime.time(2, 30)
try:
    difference = time2 - time1
except TypeError as e:
    print(f'Difference between times\t\t\t\t\t\t\t: {e}')
