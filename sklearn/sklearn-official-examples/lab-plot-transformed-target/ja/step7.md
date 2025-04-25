# エイムズ住宅データのターゲット分布をプロットする

QuantileTransformer を適用する前後のターゲットの確率密度関数をプロットします。

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("確率")
ax0.set_xlabel("ターゲット")
ax0.set_title("ターゲット分布")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("確率")
ax1.set_xlabel("ターゲット")
ax1.set_title("変換後のターゲット分布")

f.suptitle("エイムズ住宅データ：販売価格", y=1.05)
plt.tight_layout()
```
