# Богатая HTML - репрезентация

Второй способ отображения оценщиков - это богатая HTML - репрезентация. В ноутбуках оценщики и конвейеры будут использовать богатую HTML - репрезентацию. Это особенно полезно для суммаризации структуры конвейеров и других составных оценщиков с возможностью интерактивного просмотра деталей.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Создайте конвейеры для числовых и категориальных данных
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Создайте препроцессор, который применяет числовой и категориальный конвейеры к определенным столбцам
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Создайте конвейер, который применяет препроцессор и логистическую регрессию
clf = make_pipeline(preprocessor, LogisticRegression())

# Отобразите конвейер
clf
```
