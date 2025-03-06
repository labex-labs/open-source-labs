# 破線軸グラフの作成と設定

このステップでは、実際の破線軸グラフ（ブロークンアクシスプロット）の構造を作成します。破線軸グラフは、同じデータの異なる範囲を表示する複数のサブプロットで構成されます。これらのサブプロットを設定して、メインデータと外れ値（アウトライヤー）を効果的に表示します。

## サブプロットの作成

まず、垂直に配置された 2 つのサブプロットを作成する必要があります。上部のサブプロットは外れ値を表示し、下部のサブプロットは大部分のデータポイントを表示します。

ノートブックで新しいセルを作成し、以下のコードを追加します。

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Add a main title to the figure
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Display the figure to see both subplots
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

このセルを実行すると、同じデータを表示する 2 つのサブプロットがある図が表示されるはずです。両方のプロットで外れ値が残りのデータを圧縮し、大部分のデータポイントの詳細が見えにくくなっていることに注意してください。これが破線軸グラフで解決しようとしている問題です。

## Y 軸の範囲を設定する

次に、各サブプロットを特定の y 値の範囲に焦点を合わせるように設定する必要があります。上部のサブプロットは外れ値の範囲に焦点を合わせ、下部のサブプロットはメインデータの範囲に焦点を合わせます。

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

# Add a title to each subplot
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Display the figure with adjusted y-axis limits
plt.tight_layout()
plt.show()
```

このセルを実行すると、各サブプロットが異なる y 値の範囲に焦点を合わせていることがわかります。上部のプロットは外れ値のみを表示し、下部のプロットはメインデータのみを表示します。これで可視化が改善されましたが、適切な破線軸グラフにするには、さらにいくつかの設定を追加する必要があります。

## 軸の枠線を隠し、目盛りを調整する

「破線」の軸の錯覚を作り出すために、2 つのサブプロット間の接続する軸の枠線（スパイン）を隠し、目盛りの位置を調整する必要があります。

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

# Add labels to the plot
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

このセルを実行すると、2 つのサブプロット間の軸の枠線が隠され、よりクリーンな外観になっていることがわかります。x 軸の目盛りは正しく配置され、ラベルは下部にのみ表示されます。

この時点で、基本的な破線軸グラフを成功裏に作成しました。次のステップでは、軸が破線になっていることを視聴者に明確に伝えるための仕上げを行います。
