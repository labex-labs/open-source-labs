# ツールバーとVBoxにアクセスする

それぞれ `manager.toolbar` と `manager.vbox` メソッドを使って、グラフキャンバスマネージャのツールバーとvbox属性にアクセスします。

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
