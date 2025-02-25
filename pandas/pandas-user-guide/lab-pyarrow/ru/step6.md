# Чтение данных с использованием PyArrow

PyArrow предоставляет функциональность для чтения ввода-вывода (IO), которая интегрирована в несколько читателей ввода-вывода pandas.

```python
# Импортировать модуль IO
import io

# Создать объект StringIO
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# Прочитать данные в pandas DataFrame, используя PyArrow в качестве движка
df = pd.read_csv(data, engine="pyarrow")
```
