from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
