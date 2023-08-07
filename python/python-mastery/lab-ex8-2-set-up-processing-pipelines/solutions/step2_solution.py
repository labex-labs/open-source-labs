# Step 2 Solution

# ticker.py

from structure import Structure


class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()


if __name__ == "__main__":
    from follow import follow
    import csv

    lines = follow("stocklog.csv")
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
