# Almacenar datos de texto

En pandas, puede almacenar datos de texto de dos maneras: utilizando una matriz de NumPy con tipo de datos `object` o un tipo de extensión `StringDtype`. Recomendamos utilizar `StringDtype` porque es más seguro y específico que el tipo de datos genérico `object`.

```python
import pandas as pd

# crear una serie con tipo de datos `object`
s1 = pd.Series(["a", "b", "c"], dtype="object")

# crear una serie con `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
