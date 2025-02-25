# データを作成する

このステップでは、エラーバープロットを作成するために使用するデータを作成します。

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
