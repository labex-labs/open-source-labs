# Einrückung

Die Einrückung wird verwendet, um Gruppen von Anweisungen anzuzeigen, die zusammengehören. Betrachten Sie das vorherige Beispiel:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Anzahl der Tage', day)
```

Die Einrückung gruppiert die folgenden Anweisungen zusammen als die wiederholenden Operationen:

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Da die `print()`-Anweisung am Ende nicht eingerückt ist, gehört sie nicht zur Schleife. Die Leerzeile dient nur der Lesbarkeit. Sie hat keinen Einfluss auf die Ausführung.
