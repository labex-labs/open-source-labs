# フォーマッタオブジェクトによるフォーマット

このステップでは、`.Formatter` オブジェクトを使って目盛りをフォーマットします。7 つのグラフを作成し、それぞれ異なるフォーマッタを使用します。

```python
fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formatter Object Formatting')

# Null フォーマッタ
setup(axs1[0], title="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# StrMethod フォーマッタ
setup(axs1[1], title="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))

# FuncFormatter はデコレータとして使用できます
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'

setup(axs1[2], title='FuncFormatter("[{:.2f}]".format)')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Fixed フォーマッタ
setup(axs1[3], title="FixedFormatter(['A', 'B', 'C',...])")
# FixedFormatter は FixedLocator と一緒にのみ使用する必要があります。
# そうでない場合、ラベルがどこに表示されるかを確認できません。
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(positions))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# スカラーフォーマッタ
setup(axs1[4], title="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# FormatStr フォーマッタ
setup(axs1[5], title="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# パーセントフォーマッタ
setup(axs1[6], title="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
```

# フォーマッタオブジェクトによるフォーマット

このステップでは、`.Formatter` オブジェクトを使って目盛りをフォーマットします。7 つのグラフを作成し、それぞれ異なるフォーマッタを使用します。

```python
fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formatter Object Formatting')

# Null フォーマッタ
setup(axs1[0], title="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# StrMethod フォーマッタ
setup(axs1[1], title="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))

# FuncFormatter はデコレータとして使用できます
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'

setup(axs1[2], title='FuncFormatter("[{:.2f}]".format)')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Fixed フォーマッタ
setup(axs1[3], title="FixedFormatter(['A', 'B', 'C',...])")
# FixedFormatter は FixedLocator と一緒にのみ使用する必要があります。
# そうでない場合、ラベルがどこに表示されるかを確認できません。
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(positions))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# スカラーフォーマッタ
setup(axs1[4], title="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# FormatStr フォーマッタ
setup(axs1[5], title="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# パーセントフォーマッタ
setup(axs1[6], title="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
```
