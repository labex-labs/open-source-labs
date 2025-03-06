# RCParams を使用したグローバルなタイトル配置

この最後のステップでは、Matplotlib の実行時設定パラメータ (RCParams) を使用して、タイトル配置のグローバルなデフォルト値を設定する方法を学びます。これは、ノートブックやスクリプト内のすべてのプロットに一貫したタイトル配置を適用したい場合に便利で、各プロットに個別に設定する必要がありません。

## Matplotlib の RCParams の理解

Matplotlib の動作は、`rcParams` と呼ばれる辞書のような変数を使用してカスタマイズできます。これにより、タイトル配置を含むさまざまなプロパティのグローバルなデフォルト値を設定できます。

## rcParams を使用したグローバルなタイトル配置の設定

タイトル配置のグローバルなデフォルト値を設定し、これらの設定を自動的に使用するプロットを作成しましょう。

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

セルを実行して、デフォルト値を確認します。次に、これらの設定を変更しましょう。

```python
# Set new global defaults for title positioning
plt.rcParams['axes.titley'] = 1.05     # Set title y position higher
plt.rcParams['axes.titlepad'] = 10     # Set padding between title and plot
plt.rcParams['axes.titlelocation'] = 'left'  # Set default alignment to left

# Create a plot that will use the new defaults
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Global RCParams Settings')
plt.show()
```

セルを実行します。`title()` 関数で位置パラメータを指定していないにもかかわらず、タイトルが定義したグローバル設定に従って配置されていることに注意してください。

## 同じ設定を使用した複数のプロットの作成

グローバル設定をすべて使用するいくつかのプロットを作成しましょう。

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot with titles that use global settings
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1} Using Global Settings')

plt.tight_layout()
plt.show()
```

セルを実行します。4 つのサブプロットのタイトルは、前に定義したグローバル設定に従って配置されるはずです。

## RCParams をデフォルト値にリセットする

RCParams をデフォルト値にリセットしたい場合は、`rcdefaults()` 関数を使用できます。

```python
# Reset to default settings
plt.rcdefaults()

# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Default Settings Again')
plt.show()
```

セルを実行します。タイトルは Matplotlib のデフォルト設定を使用して配置されるはずです。

## RCParams の一時的な変更

コードの特定のセクションだけで RCParams を一時的に変更したい場合は、コンテキストマネージャを使用できます。

```python
# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Default Settings')
plt.show()

# Temporarily change RCParams for just this section
with plt.rc_context({'axes.titlelocation': 'right', 'axes.titley': 1.1}):
    plt.figure(figsize=(8, 5))
    plt.plot(range(10))
    plt.grid(True)
    plt.title('Temporary Settings Change')
    plt.show()

# Create another plot that will use default settings again
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Back to Default Settings')
plt.show()
```

セルを実行します。3 つのプロットが表示されるはずです。

1. 最初のプロットはデフォルトのタイトル配置
2. 2 番目のプロットは右寄せで高い位置にタイトルが配置されています（一時的な設定のため）
3. 3 番目のプロットは再びデフォルトのタイトル配置（一時的な設定はコンテキストマネージャ内でのみ適用されるため）

このアプローチにより、他のプロットに影響を与えることなく、グローバル設定を一時的に変更することができます。
