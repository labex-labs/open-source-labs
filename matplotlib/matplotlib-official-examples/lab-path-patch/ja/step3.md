# PathPatch オブジェクトの作成

このステップでは、前のステップで作成したパスオブジェクトを使用して`PathPatch`オブジェクトを作成します。このオブジェクトは、パスで囲まれた領域を塗りつぶすために使用されます。また、パッチの色や透明度を設定することもできます。

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
