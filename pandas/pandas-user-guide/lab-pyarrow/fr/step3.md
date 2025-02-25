# Utilisation de types PyArrow avec des paramètres

Pour les types PyArrow qui acceptent des paramètres, vous pouvez passer un type PyArrow avec ces paramètres à `ArrowDtype` pour l'utiliser dans le paramètre `dtype`.

```python
# Importez PyArrow
import pyarrow as pa

# Créez une série pandas avec un type de liste PyArrow
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
