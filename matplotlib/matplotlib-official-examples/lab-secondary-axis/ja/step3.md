# 二次軸を作成する

ここでは、二次軸を作成し、x 軸を度数からラジアンに変換します。順方向の関数として`deg2rad`を、逆方向の関数として`rad2deg`を使用します。

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
