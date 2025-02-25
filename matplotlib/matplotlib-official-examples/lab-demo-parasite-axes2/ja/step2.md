# ホスト軸と寄生虫軸の作成

`host_subplot()`と`twinx()`関数を使って、ホスト軸と2つの寄生虫軸を作成します。`host_subplot()`関数はホスト軸を作成し、`twinx()`関数はホスト軸と同じx軸を共有する寄生虫軸を作成します。

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
