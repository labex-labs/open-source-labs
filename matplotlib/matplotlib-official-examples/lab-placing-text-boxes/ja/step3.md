# 統計情報を含むテキストボックスの追加

基本的なヒストグラムができたので、データの統計情報を表示するテキストボックスを追加して、ビジュアライゼーションを充実させましょう。これにより、閲覧者にとってビジュアライゼーションがより有益なものになります。

## テキスト内容の作成

まず、テキストボックス内に表示するテキスト内容を準備する必要があります。新しいセルに以下のコードを入力して実行します。

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

以下のような出力が表示されるはずです。

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

このコードは、データの平均、中央値、標準偏差を含む複数行の文字列を作成します。このコードの興味深い点を見てみましょう。

1. `\n'.join(...)` メソッドは、複数の文字列を改行文字で結合します。
2. 各文字列の前の `r` は、その文字列を「生の」文字列にします。これは特殊文字を含む場合に便利です。
3. `$...$` 表記は、matplotlib で LaTeX スタイルの数式を書式設定するために使用されます。
4. `\mu` と `\sigma` は、ギリシャ文字の μ（ミュー）と σ（シグマ）の LaTeX 記号です。
5. `%.2f` は、浮動小数点数を小数点以下2桁で表示する書式指定子です。

## テキストボックスの作成と追加

次に、ヒストグラムを再作成し、テキストボックスを追加しましょう。新しいセルに以下のコードを入力して実行します。

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

このセルを実行すると、左上隅に統計情報を表示するテキストボックスが付いたヒストグラムが表示されます。

## テキストボックスのコードの理解

テキストボックスを作成するコードの重要な部分を分解してみましょう。

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:

   - これは、テキストボックスのプロパティを持つ辞書を作成します。
   - `boxstyle='round'`：ボックスの角を丸くします。
   - `facecolor='wheat'`：ボックスの背景色を小麦色に設定します。
   - `alpha=0.5`：ボックスを半透明にします（不透明度50%）。

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - これは、位置 (0.05, 0.95) にテキストを軸に追加します。
   - `transform=ax.transAxes`：これは重要です。座標がデータ単位ではなく軸単位（0 - 1）であることを意味します。したがって、(0.05, 0.95) は「グラフの左端から5%、下端から95%」を意味します。
   - `fontsize=14`：フォントサイズを設定します。
   - `verticalalignment='top'`：テキストの上部が指定されたy座標に位置するようにテキストを配置します。
   - `bbox=properties`：テキストボックスのプロパティを適用します。

テキストボックスは、グラフを拡大したりデータ範囲を変更したりしても、グラフの軸に対して同じ位置に留まります。これは、`transform=ax.transAxes` を使用して軸座標を使用したためです。
