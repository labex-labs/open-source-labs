# Загрузка датасета

Мы загрузим датасет 20 newsgroups и векторизуем его. Мы используем несколько эвристик для предварительного фильтрации бесполезных терминов: из постов удаляются заголовки, подписи и цитируемые ответы, а также общие английские слова, слова, встречающиеся только в одном документе или в по крайней мере 95% документов.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Loading dataset...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
