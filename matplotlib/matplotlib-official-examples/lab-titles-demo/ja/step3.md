# タイトルの垂直位置のカスタマイズ

時には、タイトルの垂直位置を調整したいことがあるかもしれません。このステップでは、プロットのタイトルの垂直（y 軸）位置を手動で制御する方法を学びます。

## タイトルの Y 位置の理解

タイトルの垂直位置は、`title()` 関数の `y` パラメータを使用して調整できます。`y` パラメータは正規化された座標の値を受け取り、以下のように動作します。

- `y = 1.0`（デフォルト）はタイトルをプロットの上部に配置します。
- `y > 1.0` はタイトルをプロットの上部より上に配置します。
- `y < 1.0` はタイトルをプロットの上部より下に配置し、プロットの内容に近づけます。

## カスタム Y 位置のタイトルを持つプロットの作成

タイトルをデフォルトよりも高い位置に配置したプロットを作成しましょう。新しいセルに以下のコードを入力します。

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

セルを実行します。タイトルがデフォルト位置と比較してプロットの少し上に表示されることに注意してください。

次に、タイトルをデフォルトよりも低い位置に配置したプロットを作成しましょう。

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

セルを実行します。タイトルはプロットの内容に近く表示されるはずです。

## 異なる Y 位置の比較

異なる垂直タイトル位置を比較するために、複数のプロットを並べて作成しましょう。

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

セルを実行して、3 つの垂直位置を並べて表示します。この比較により、`y` パラメータがタイトルの垂直位置にどのように影響するかを理解することができます。

## 水平位置と垂直位置の組み合わせ

`loc` パラメータ（水平位置調整用）と `y` パラメータ（垂直位置調整用）を組み合わせることで、タイトルを正確に希望の位置に配置することができます。

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

セルを実行します。タイトルはプロットの右側に配置され、デフォルトよりも高い位置に表示されるはずです。
