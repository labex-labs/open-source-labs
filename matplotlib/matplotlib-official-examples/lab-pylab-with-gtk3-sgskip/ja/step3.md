# ツールバーと VBox にアクセスする

それぞれ `manager.toolbar` と `manager.vbox` メソッドを使って、グラフキャンバスマネージャのツールバーと vbox 属性にアクセスします。

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
