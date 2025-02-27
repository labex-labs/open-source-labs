# Representación de texto compacta

La primera forma en que podemos mostrar estimadores es a través de la representación de texto compacta. Los estimadores solo mostrarán los parámetros que se han establecido en valores no predeterminados cuando se muestran como una cadena. Esto reduce el ruido visual y facilita la detección de diferencias al comparar instancias.

```python
from sklearn.linear_model import LogisticRegression

# Crea una instancia de Regresión Logística con penalización l1
lr = LogisticRegression(penalty="l1")

# Muestra el estimador
print(lr)
```
