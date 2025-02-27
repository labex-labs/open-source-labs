# Dataset

Wir werden das 20 newsgroups-Dataset verwenden, das aus Beiträgen von Newsgroups zu 20 Themen besteht. Das Dataset wird in Trainings- und Testuntersetzungen aufgeteilt, basierend auf Nachrichten, die vor und nach einem bestimmten Datum veröffentlicht wurden. Wir werden nur Beiträge aus 2 Kategorien verwenden, um die Laufzeit zu beschleunigen.

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
