# マスク付きの風羽図の作成

マスク付き配列を使って、マスク付きの風羽図も作成できます。この場合、1 つのベクトルの値を不適切な値に変更してマスクします。

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # マスクされたときにプロットされるべきではない不適切な値
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
