# パッチの作成

パッチを作成するには、Matplotlibの`patches`モジュールを使用します。半径200ピクセルの円形のパッチを、点(260, 200)を中心に作成します。

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
