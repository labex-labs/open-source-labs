# 使用 PyArrow 读取数据

PyArrow 提供了已集成到多个 pandas IO 读取器中的 IO 读取功能。

```python
# 导入 IO 模块
import io

# 创建一个 StringIO 对象
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# 使用 PyArrow 作为引擎将数据读入 pandas DataFrame
df = pd.read_csv(data, engine="pyarrow")
```
