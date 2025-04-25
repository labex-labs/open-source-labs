# テキストの配置とスタイルの制御

Matplotlib のプロット内のテキストの配置とスタイルも制御できます。スクリプトに次のコードを追加してみてください。

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

これにより、プロットに 4 つのテキスト要素が追加され、それぞれ異なる色、フォントサイズ、位置が設定されます。
