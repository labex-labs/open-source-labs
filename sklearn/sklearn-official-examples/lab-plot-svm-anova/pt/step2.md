# Criar o Pipeline

Em seguida, criamos um pipeline composto por uma transformação de seleção de características, um escalador e uma instância de SVM que combinamos para obter um estimador completo.

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
