# Definir os Classificadores

Definiremos dois classificadores diferentes para comparar seu desempenho estatístico em diferentes limiares usando as curvas ROC e DET. Usaremos a função `make_pipeline` do scikit-learn para criar um pipeline que escala os dados usando `StandardScaler` e treina um classificador `LinearSVC`. Também usaremos a classe `RandomForestClassifier` do scikit-learn para treinar um classificador de floresta aleatória com profundidade máxima de 5, 10 estimadores e um máximo de 1 característica.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
