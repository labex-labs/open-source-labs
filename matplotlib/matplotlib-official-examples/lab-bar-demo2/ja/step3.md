# 既定の単位で棒グラフを作成する

このステップでは、Matplotlibの`bar`メソッドを使って既定の単位で棒グラフを作成します。棒の下端を0に設定するために`bottom`パラメータを使用します。

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
