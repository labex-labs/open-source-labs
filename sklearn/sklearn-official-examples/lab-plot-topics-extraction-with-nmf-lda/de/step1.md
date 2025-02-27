# Lade den Datensatz

Wir werden den 20 Newsgroups-Datensatz laden und ihn vektorisieren. Wir verwenden einige Heuristiken, um frühzeitig nutzlose Begriffe zu filtern: Die Beiträge werden von Kopfzeilen, Fußzeilen und zitierten Antworten befreit, und übliche englische Wörter, Wörter, die nur in einem Dokument oder in mindestens 95% der Dokumente auftauchen, werden entfernt.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Lade Datensatz...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
