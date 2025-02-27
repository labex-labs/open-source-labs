# クラスと特徴の確率を表示する

最後に、`plot_2d`関数が返すクラス確率と特徴確率を使って、各クラスのクラスと特徴の確率を表示します。

```python
print("The data was generated from (random_state=%d):" % RANDOM_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep="\t")
for k, p, p_w in zip(["red", "blue", "yellow"], p_c, p_w_c.T):
    print("%s\t%0.2f\t%0.2f\t%0.2f" % (k, p, p_w[0], p_w[1]))
```
