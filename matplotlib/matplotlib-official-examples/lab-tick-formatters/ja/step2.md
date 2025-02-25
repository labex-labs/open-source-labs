# 単純なフォーマット

このステップでは、文字列を渡すか関数を `~.Axis.set_major_formatter` または `~.Axis.set_minor_formatter` に渡すことで、単純なフォーマッタをどのように使用するかを示します。2つのグラフを作成し、1つは文字列フォーマッタを使用し、もう1つは関数フォーマッタを使用します。

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# ``str`` は、フォーマット文字列関数構文を使用して、直接フォーマッタとして使用できます。
# 変数 ``x`` は目盛り値で、変数 ``pos`` は目盛り位置です。
# これにより、自動的に StrMethodFormatter が作成されます。
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# 関数も直接フォーマッタとして使用できます。
# この関数は2つの引数を取る必要があります。
# 目盛り値用の ``x`` と目盛り位置用の ``pos`` で、
# そして ``str`` を返す必要があります。
# これにより、自動的に FuncFormatter が作成されます。
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```

# 単純なフォーマット

このステップでは、文字列を渡すか関数を `~.Axis.set_major_formatter` または `~.Axis.set_minor_formatter` に渡すことで、単純なフォーマッタをどのように使用するかを示します。2つのグラフを作成し、1つは文字列フォーマッタを使用し、もう1つは関数フォーマッタを使用します。

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# 「str」は、フォーマット文字列関数構文を使用して、直接フォーマッタとして使用できます。
# 変数「x」は目盛り値で、変数「pos」は目盛り位置です。
# これにより、自動的にStrMethodFormatterが作成されます。
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# 関数も直接フォーマッタとして使用できます。
# この関数は2つの引数を取る必要があります。
# 目盛り値用の「x」と目盛り位置用の「pos」で、
# そして「str」を返す必要があります。
# これにより、自動的にFuncFormatterが作成されます。
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
