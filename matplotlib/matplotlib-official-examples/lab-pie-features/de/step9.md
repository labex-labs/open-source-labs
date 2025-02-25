# Die Schatten ändern

Wir können den Schatten des Kreisdiagramms ändern, indem wir ein Argument-Dictionary an den `shadow`-Parameter der `pie()`-Funktion übergeben.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```
