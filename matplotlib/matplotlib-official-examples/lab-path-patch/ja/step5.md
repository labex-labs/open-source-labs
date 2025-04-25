# 制御点と接続線をプロットする

このステップでは、axes オブジェクトの`plot`メソッドを使って、パスの制御点と接続線をプロットします。

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
