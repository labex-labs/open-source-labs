# PyArrow 로 데이터 읽기

PyArrow 는 여러 pandas IO 리더에 통합된 IO 읽기 기능을 제공합니다.

```python
# Import IO module
import io

# Create a StringIO object
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Read the data into a pandas DataFrame using PyArrow as the engine
df = pd.read_csv(data, engine="pyarrow")
```
