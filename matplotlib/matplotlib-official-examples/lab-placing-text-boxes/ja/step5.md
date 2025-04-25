# 複数のテキスト要素を持つ最終的なビジュアライゼーションの作成

この最後のステップでは、これまで学んだことをすべて組み合わせて、異なるスタイルの複数のテキスト要素を含む包括的なビジュアライゼーションを作成します。これにより、テキストボックスがデータストーリーテリングを強化するためにどのように使用できるかを示します。

## 高度なビジュアライゼーションの作成

ヒストグラムといくつかの追加の視覚要素を含む、より洗練されたグラフを作成しましょう。新しいセルに以下のコードを入力して実行します。

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

このセルを実行すると、以下の要素を含む包括的なビジュアライゼーションが表示されます。

- スタイルが改善されたデータのヒストグラム
- 平均と 1 標準偏差の範囲を示す垂直線
- 左上隅にある統計情報のテキストボックス
- 右上隅にある正規分布に関する情報のテキストボックス
- 垂直線の意味を説明する凡例

## 高度な要素の理解

追加した新しい要素のいくつかを見てみましょう。

1. **`axvline()` を使用した垂直線**：

   - これらの線は、グラフ上に重要な統計情報を直接示します。
   - `label` パラメータにより、これらの線を凡例に含めることができます。

2. **異なるスタイルの複数のテキストボックス**：

   - 各テキストボックスは異なる目的を持ち、独特のスタイルを使用しています。
   - 統計情報のボックスは、データから計算された値を表示します。
   - 情報ボックスは、正規分布に関するコンテキストを提供します。

3. **強化された書式設定**：

   - LaTeX の書式設定を使用して、`\mathbf{}` で太字のテキストを作成します。
   - `\bullet` で箇条書きを作成します。
   - `\ `（バックスラッシュの後にスペース）で間隔を制御します。

4. **グリッドと凡例**：
   - グリッドは、閲覧者がチャートから値をより正確に読み取るのに役立ちます。
   - 凡例は、色付きの線の意味を説明します。

## テキストボックス配置に関する最後の注意点

ビジュアライゼーションに複数のテキスト要素を配置する際には、以下の点を考慮してください。

1. **視覚的な階層**：最も重要な情報は最も目立つようにする必要があります。
2. **配置**：関連する情報をビジュアライゼーションの関連部分の近くに配置します。
3. **コントラスト**：テキストが背景に対して読みやすいことを確認します。
4. **一貫性**：同じ種類の情報には一貫したスタイルを使用します。
5. **混雑**：ビジュアライゼーションに過度に多くのテキスト要素を配置しないようにします。

テキストボックスを慎重に配置し、スタイルを設定することで、情報が豊富で視覚的に魅力的なビジュアライゼーションを作成し、閲覧者がデータから重要な洞察を理解するのを導くことができます。
