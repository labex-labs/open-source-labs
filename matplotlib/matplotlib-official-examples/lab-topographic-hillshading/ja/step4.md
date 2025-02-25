# 光源とカラーマップを指定する

光源の方位角と高度を設定することで、LightSourceオブジェクトを指定します。また、プロットで使用するカラーマップも設定します。

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
