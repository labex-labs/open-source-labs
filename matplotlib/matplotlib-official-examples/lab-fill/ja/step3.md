# 塗りつぶされた多角形を生成する

今、`fill()` 関数を使って塗りつぶされた多角形を生成することができます。多角形の座標を生成するためにコッホの雪花関数を使います。

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
