# Leyendo Datos con PyArrow

PyArrow proporciona funcionalidad de lectura de E/S que se ha integrado en varios lectores de E/S de pandas.

```python
# Importa el módulo de E/S
import io

# Crea un objeto StringIO
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Lee los datos en un DataFrame de pandas utilizando PyArrow como motor
df = pd.read_csv(data, engine="pyarrow")
```
