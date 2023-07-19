import calendar


def determine_what_day_of_the_week():
    month, day, year = map(int, input().split())

    dayId = calendar.weekday(year, month, day)
    print(calendar.day_name[dayId].upper())


determine_what_day_of_the_week()
