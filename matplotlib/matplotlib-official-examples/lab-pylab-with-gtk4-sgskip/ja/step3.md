# ツールバーと vbox にアクセスする

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

グラフキャンバスマネージャの `toolbar` と `vbox` 属性にアクセスします。
