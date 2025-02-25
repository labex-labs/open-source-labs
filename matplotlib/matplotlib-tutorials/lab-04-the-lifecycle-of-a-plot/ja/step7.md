# グラフを保存する

最後に、グラフをディスクに保存することができます。以下の手順に従ってください。

1. `print(fig.canvas.get_supported_filetypes())` を使用して、サポートされているファイル形式を表示します。

```python
print(fig.canvas.get_supported_filetypes())
```

2. `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")` を使用して、画像ファイルとしてグラフを保存します。この行のコメントを解除してグラフを保存します。

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

左側のサイドバーにあるファイルエクスプローラーを使用して、保存した画像ファイルを開くことができます。
