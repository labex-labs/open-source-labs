# Загрузка данных и обучение модели

Для примера мы будем использовать набор данных центра по переливанию крови из OpenML. Целевой признак - это, донорствовал ли человек кровь или нет. Сначала данные разделяются на обучающую и тестовую выборки, а затем на обучающей выборке подбирается логистическая регрессионная модель.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```
