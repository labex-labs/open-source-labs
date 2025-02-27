# Obtener las probabilidades de clase para la primera muestra del conjunto de datos

Obtendremos las probabilidades de clase para la primera muestra del conjunto de datos y las almacenaremos en class1_1 y class2_1.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
