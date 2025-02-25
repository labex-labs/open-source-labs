# 各一次3Dビュープレーンの目盛りラベルと軸ラベルをカスタマイズする

各一次3Dビュープレーンの目盛りラベルと軸ラベルをカスタマイズして、不要なラベルを削除します。

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
