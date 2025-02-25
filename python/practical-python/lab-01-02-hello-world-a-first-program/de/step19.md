# Übung 1.6: Debugging

Der folgende Codeausschnitt enthält Code aus dem Sears Tower - Problem. Es hat auch einen Fehler darin.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meter (0.11 mm)
sears_height   = 442             # Höhe (Meter)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Anzahl der Tage', day)
print('Anzahl der Scheine', num_bills)
print('Endhöhe', num_bills * bill_thickness)
```

Kopieren Sie und fügen Sie den obigen Code in ein neues Programm namens `sears.py` ein. Wenn Sie den Code ausführen, erhalten Sie eine Fehlermeldung, die das Programm zum Abstürzen bringt, wie folgt:

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

Das Lesen von Fehlermeldungen ist ein wichtiger Teil von Python - Code. Wenn Ihr Programm abstürzt, ist die letzte Zeile der Traceback - Meldung der tatsächliche Grund, warum das Programm abstürzt. Darunter sollten Sie einen Codeausschnitt, dann eine Dateiname - und Zeilennummer - Kennung sehen.

- Welche Zeile ist der Fehler?
- Was ist der Fehler?
- Beheben Sie den Fehler
- Führen Sie das Programm erfolgreich aus
