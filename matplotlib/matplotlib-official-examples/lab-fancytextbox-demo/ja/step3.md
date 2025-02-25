# もう1つのテキストボックスを作成する

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

「spam」という単語が入ったもう1つのテキストボックスを作成します。今回は、四角いボックスを作成するために `boxstyle` パラメータを "square" に設定し、ボックスの右側と上部にテキストを整列させるために `ha` と `va` パラメータを "right" と "top" に設定します。
