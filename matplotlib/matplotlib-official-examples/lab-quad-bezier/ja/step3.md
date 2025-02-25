# PathPatchオブジェクトの作成

`Path`オブジェクトができたので、これを使ってグラフ上にベジェ曲線を描画するための`PathPatch`オブジェクトを作成できます。塗りつぶされるのではなく、曲線のみを描画するように`facecolor`を`'none'`に設定します。

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
