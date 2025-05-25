# Lendo Dados com PyArrow

PyArrow fornece funcionalidade de leitura de IO que foi integrada em vários leitores de IO do pandas.

```python
# Import IO module
import io

# Create a StringIO object
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Read the data into a pandas DataFrame using PyArrow as the engine
df = pd.read_csv(data, engine="pyarrow")
```
