# Reading Data with PyArrow

PyArrow provides IO reading functionality that has been integrated into several pandas IO readers.

```python
# Import IO module
import io

# Create a StringIO object
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Read the data into a pandas DataFrame using PyArrow as the engine
df = pd.read_csv(data, engine="pyarrow")
```
