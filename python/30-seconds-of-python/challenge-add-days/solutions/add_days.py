from datetime import datetime, timedelta


def add_days(n, d=datetime.today()):
    return d + timedelta(n)
