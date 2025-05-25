# Criar ConfusionMatrixDisplay

Com o modelo ajustado, calculamos as previsões do modelo no conjunto de dados de teste. Essas previsões são usadas para calcular a matriz de confusão, que é plotada com o `ConfusionMatrixDisplay`.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
