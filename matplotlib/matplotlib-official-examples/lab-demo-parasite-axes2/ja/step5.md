# 軸の範囲とラベルの設定

`set()`関数を使用して、各軸の x 軸と y 軸の範囲とラベルを設定します。

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
