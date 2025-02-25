# 接続線の描画

5 番目のステップは、2 つのサブプロットを結ぶ点線を描画することです。左のサブプロットの原点と右のサブプロットの右辺を結ぶ `ConnectionPatch` オブジェクトを作成します。また、アニメーションの後半で更新する `con` パッチオブジェクトを保存します。

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
