# 目盛りとラベルのカスタマイズ

`ax1.tick_params()` メソッドを使って、軸の目盛りとラベルをカスタマイズします。x 軸のラベルの色、回転、サイズを設定し、y 軸の目盛りの色、サイズ、幅を設定します。

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
