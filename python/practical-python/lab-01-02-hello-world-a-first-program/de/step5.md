# Ein Beispielprogramm

Lösen wir folgendes Problem:

> Eines Morgens gehst du hinaus und legst einen Dollar-Schein auf den Bürgersteig neben dem Sears Tower in Chicago. Danach gehst du jeden Tag hinaus und verdoppelt die Anzahl der Scheine. Wie lange dauert es, bis der Stapel von Scheinen die Höhe des Turms überschreitet?

Hier ist eine Lösung, um eine `sears.py`-Datei im Verzeichnis `/home/labex/project` zu erstellen:

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meter (0.11 mm)
sears_height = 442 # Höhe (Meter)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Anzahl der Tage', day)
print('Anzahl der Scheine', num_bills)
print('Endhöhe', num_bills * bill_thickness)
```

Wenn Sie es ausführen, erhalten Sie die folgende Ausgabe:

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Anzahl der Tage 23
Anzahl der Scheine 4194304
Endhöhe 461.37344
```

Anhand dieses Programms können Sie eine Reihe wichtiger Kernkonzepte von Python lernen.
