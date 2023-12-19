import datetime
import pytz

data = datetime.datetime.now(tz=pytz.timezone('Asia/Tashkent'))


dtdelta = datetime.timedelta(minutes=12)

print(data+dtdelta)


# eng_date = 'December 19, 2023'
# date = datetime.datetime.strptime(eng_date, '%B %d, %Y')
# print(date)


# print(data.strftime('%B %d, %Y - %H hour %M minutes %S seconds, %A, %W'))


# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_utc = dt_now.astimezone(pytz.timezone('Asia/Samarkand'))
# print(dt_utc)


# for i in pytz.all_timezones:
#     print(i)
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# dt_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)


# print(dt_today)
# print(dt_now)
# print(dt_utc)

# tkun = datetime.date(2024,5,22)



# print(tkun)


# print(tkun-data)

# tdelda = datetime.timedelta(weeks=1)
# print( data - tdelda)


# data.isoweekday() Dushanba 1dan Yakshanba 7
# data.weekday() Dushanba 0dan Yakshanba 6
