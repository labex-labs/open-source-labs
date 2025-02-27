# Daten laden

Wir werden Daten aus `20newsgroups_dataset` laden, das aus rund 18.000 Newsgroup-Posts zu 20 Themen besteht, die in zwei Teilmengen unterteilt sind: eine für das Training und eine für das Testing. Aus Gründen der Einfachheit und zur Reduzierung der Rechenkosten wählen wir eine Teilmenge von 7 Themen und verwenden nur den Trainingssatz.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("Loading 20 newsgroups training data")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documents - {data_size_mb:.3f}MB")
```
