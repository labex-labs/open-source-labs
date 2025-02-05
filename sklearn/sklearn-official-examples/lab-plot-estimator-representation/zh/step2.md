# 丰富的HTML表示

我们可以通过丰富的HTML表示来显示估计器，这是显示估计器的第二种方式。在笔记本中，估计器和管道将使用丰富的HTML表示。这对于总结管道和其他复合估计器的结构特别有用，并且具有提供详细信息的交互性。

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# 为数值型和分类型数据创建管道
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore")
)

# 创建一个预处理器，将数值型和分类型管道应用于特定列
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# 创建一个应用预处理器和逻辑回归的管道
clf = make_pipeline(preprocessor, LogisticRegression())

# 显示管道
clf
```
