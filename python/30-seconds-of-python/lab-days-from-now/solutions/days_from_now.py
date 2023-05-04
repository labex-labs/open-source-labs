from datetime import timedelta, date


def days_from_now(n):
    return date.today() + timedelta(n)
