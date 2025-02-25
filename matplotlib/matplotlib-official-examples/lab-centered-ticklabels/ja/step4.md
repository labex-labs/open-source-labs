# 大目盛りラベルと小目盛りを削除する

目盛りの間にラベルを中央に配置する動作を疑似的に再現するには、大目盛りラベルと小目盛りを削除し、小目盛りラベルのみを表示する必要があります。これは`tick_params()`関数を使って、`tick1On`と`tick2On`パラメータを`False`に設定することで行えます。

```python
# 目盛り線を削除する
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
