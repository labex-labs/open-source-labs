# Einrückung - Beste Praktiken

- Verwenden Sie Leerzeichen statt Tabulatoren.
- Verwenden Sie 4 Leerzeichen pro Einrückungsebene.
- Verwenden Sie einen Python-fähigen Editor.

Python erfordert lediglich, dass die Einrückung innerhalb desselben Blocks konsistent ist. Beispielsweise ist dies ein Fehler:

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # FEHLER
    num_bills = num_bills * 2
```
