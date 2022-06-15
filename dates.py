import datetime

dates = []
today = datetime.date.today()
for i in range(7):
    dates.append(str(today + datetime.timedelta(days=i)))


print(dates)
