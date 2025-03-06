# 破線軸グラフの仕上げ

この最後のステップでは、破線軸グラフ（ブロークンアクシスプロット）に仕上げを加え、y 軸が破線になっていることを明確にします。サブプロット間に斜線を追加して破線部分を示し、適切なラベルとグリッドを追加してグラフの全体的な外観を改善します。

## 斜線の破線を追加する

軸が破線になっていることを視覚的に示すために、2 つのサブプロット間に斜線を追加します。これは、軸の一部が省略されていることを視聴者に理解させるための一般的な慣習です。

新しいセルを作成し、以下のコードを追加します。

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

このセルを実行すると、y 軸の破線部分を示す斜線が付いた完全な破線軸グラフが表示されるはずです。グラフにはタイトル、軸ラベル、グリッド線が追加され、読みやすさが向上しています。

## 破線軸グラフの理解

破線軸グラフの主要な構成要素を理解するために少し時間を取りましょう。

1. **2 つのサブプロット**：異なる y 値の範囲に焦点を合わせた 2 つの別々のサブプロットを作成しました。
2. **隠された軸の枠線**：サブプロット間の接続する軸の枠線（スパイン）を隠して、視覚的な分離を作成しました。
3. **斜線の破線**：軸が破線になっていることを示すために斜線を追加しました。
4. **Y 軸の範囲**：各サブプロットに異なる y 軸の範囲を設定して、データの特定の部分に焦点を合わせました。
5. **グリッド線**：読みやすさを向上させ、値を推定しやすくするためにグリッド線を追加しました。

この手法は、データに外れ値（アウトライヤー）があり、それが大部分のデータポイントの可視化を圧縮してしまう場合に特に有用です。軸を「破線」にすることで、外れ値とメインのデータ分布の両方を 1 つの図で明確に表示できます。

## グラフを試す

破線軸グラフの作成方法がわかったので、さまざまな設定を試すことができます。y 軸の範囲を変更したり、グラフにさらに機能を追加したり、この手法を自分のデータに適用したりしてみてください。

たとえば、前のコードを変更して凡例を追加したり、配色を変更したり、マーカーのスタイルを調整したりできます。

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

この拡張されたコードを実行すると、外れ値が特別にマークされ、データポイントを説明する凡例が付いた改善された可視化が表示されるはずです。

おめでとうございます！Matplotlib を使用して Python で破線軸グラフを成功裏に作成しました。この手法は、外れ値を含むデータを扱う際に、より効果的な可視化を作成するのに役立ちます。
