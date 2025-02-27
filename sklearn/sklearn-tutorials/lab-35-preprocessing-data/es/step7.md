# Creación de Transformadores Personalizados

En algunos casos, puede que queramos convertir una función de Python existente en un transformador para ayudar en la limpieza o procesamiento de datos. Podemos lograr esto utilizando el `FunctionTransformer` de scikit-learn.

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# Crea una función personalizada
def custom_function(X):
    return np.log1p(X)

# Inicializa el FunctionTransformer
transformer = FunctionTransformer(custom_function)

# Crea un conjunto de datos de muestra
X = np.array([[0, 1],
              [2, 3]])

# Transforma los datos utilizando la función personalizada
X_transformed = transformer.transform(X)

# Imprime los datos transformados
print
```

需要注意的是，你提供的原始英文内容中最后一个`print`语句后面缺少参数，这可能会导致代码运行出错。翻译后的内容保留了原始代码的问题。
