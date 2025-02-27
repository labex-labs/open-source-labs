# Загрузка данных

Мы загрузим данные из `20newsgroups_dataset`, который содержит около 18000 публикаций новостных групп по 20 темам, разделенных на две подмножества: одно для обучения, а другое для тестирования. Для простоты и снижения вычислительных затрат мы выбираем подмножество из 7 тем и используем только обучающий набор.

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
