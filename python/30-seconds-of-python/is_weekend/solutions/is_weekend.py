from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
