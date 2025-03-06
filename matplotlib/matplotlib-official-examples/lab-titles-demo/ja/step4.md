# サブプロットを使用した高度なタイトル配置

このステップでは、サブプロットレイアウトと軸オブジェクトを使用する際の高度なタイトル配置技術を学びます。また、複数のサブプロットを持つ図に全体的なタイトルを追加するための `suptitle()` 関数の使い方も学びます。

## サブプロットと個別のタイトルを持つ図の作成

それぞれ異なる位置にタイトルが配置された 2x2 のサブプロットグリッドを作成しましょう。

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

セルを実行します。それぞれ異なる位置にタイトルが配置された 4 つのサブプロットが表示されるはずです。

## suptitle() を使用した図レベルのタイトルの追加

複数のサブプロットを使用する場合、図全体に対する全体的なタイトルを追加したいことがあります。これは `suptitle()` 関数を使用して行うことができます。

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

セルを実行します。それぞれ独自のタイトルを持つ 4 つのサブプロットと、図の上部に全体的なタイトルが表示されるはずです。

## 軸タイトルと図タイトルの組み合わせ

個別のサブプロットタイトルと全体的な図タイトルを組み合わせることができます。

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

セルを実行します。それぞれ異なる位置にタイトルが配置された 4 つのサブプロットと、図の上部に全体的なタイトルが表示されるはずです。

`suptitle()` 関数は、図全体を説明するメインタイトルを追加するのに便利です。一方、軸オブジェクトに対する個別の `set_title()` 呼び出しは、各サブプロットにより具体的なタイトルを追加します。
