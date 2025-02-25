# ステムプロットの作成

次に、近接するイベントを区別するために、レベルにいくつかの変化を持つステムプロットを作成します。タイムラインの一次元的な性質を視覚的に強調するために、基準線にマーカーを追加します。各イベントに対して、`~.Axes.annotate`を使用してテキストラベルを追加し、イベント線の先端からポイント単位でオフセットさせます。以下はステムプロットを作成するコードです。

```python
# いくつかの良いレベルを選ぶ
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# グラフを作成し、日付付きのステムプロットを描画する
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # 垂直の茎
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # 基準線とその上のマーカー

# 線に注釈を付ける
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
