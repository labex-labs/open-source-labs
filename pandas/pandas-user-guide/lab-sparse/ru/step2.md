# Проверка эффективности использования памяти

Далее мы проверим эффективность использования памяти при работе с разреженными структурами данных. Создадим большой DataFrame, преобразуем его в разреженный и сравним объем памяти, занимаемый обоими вариантами.

```python
# Creating a large DataFrame with random values
df = pd.DataFrame(np.random.randn(10000, 4))

# Setting majority of the DataFrame to NaN
df.iloc[:9998] = np.nan

# Converting the DataFrame to sparse
sdf = df.astype(pd.SparseDtype("float", np.nan))

# Checking memory usage of dense vs sparse DataFrame
print('dense : {:0.2f} bytes'.format(df.memory_usage().sum() / 1e3))
print('sparse: {:0.2f} bytes'.format(sdf.memory_usage().sum() / 1e3))
```
