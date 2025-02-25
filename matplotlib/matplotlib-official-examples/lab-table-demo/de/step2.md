# Erstellen des Datensatzes

Als nächstes werden wir einen Beispiel-Datensatz erstellen, um die Verluste, die durch verschiedene Naturkatastrophen in den vergangenen Jahren verursacht wurden, zu visualisieren. Wir werden eine zweidimensionale Liste verwenden, um die Daten zu speichern, und einen Tuple, um die Spaltennamen zu speichern.

```python
data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
```
