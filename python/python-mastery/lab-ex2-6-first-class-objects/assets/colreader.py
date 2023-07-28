# colreader.py

import collections
import csv


class DataCollection(collections.Sequence):
    def __init__(self, columns):
        self.column_names = list(columns)
        self.column_data = list(columns.values())

    def __len__(self):
        return len(self.column_data[0])

    def __getitem__(self, index):
        return dict(zip(self.column_names, (col[index] for col in self.column_data)))


def read_csv_as_columns(filename, types):
    pass
    # TODO: implement this function

if __name__ == "__main__":
    import tracemalloc
    from sys import intern

    tracemalloc.start()
    data = read_csv_as_columns("/home/labex/project/ctabus.csv", [intern, intern, intern, int])
    print(tracemalloc.get_traced_memory())
