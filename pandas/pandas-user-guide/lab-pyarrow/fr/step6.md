# Lecture de données avec PyArrow

PyArrow fournit des fonctionnalités de lecture d'entrée/sortie (IO) qui ont été intégrées dans plusieurs lecteurs d'IO de pandas.

```python
# Importez le module IO
import io

# Créez un objet StringIO
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Lisez les données dans un DataFrame pandas en utilisant PyArrow comme moteur
df = pd.read_csv(data, engine="pyarrow")
```
