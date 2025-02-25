# Aliase

Um die Anzahl der erforderlichen Tastatureingaben im interaktiven Modus zu reduzieren, haben eine Reihe von Eigenschaften kurze Aliase, z. B. 'lw' für 'linewidth' und'mec' für'markeredgecolor'. Wenn Sie set oder get im Introspektionsmodus aufrufen, werden diese Eigenschaften als 'vollständiger Name' oder 'Aliasname' aufgelistet.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```
