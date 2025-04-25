# パスの作成

次に、ベジェ曲線用の`Path`オブジェクトを作成します。`Path`オブジェクトは、頂点のリストと、頂点間のパスの種類を指定するコードを受け取ります。この場合、始点に移動するために`MOVETO`コードを使用し、次に制御点と終点を指定する 2 つの`CURVE3`コードを使用し、最後にパスを閉じるために`CLOSEPOLY`コードを使用します。

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
