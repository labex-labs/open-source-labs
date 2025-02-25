# ライターを設定する

フレームをファイルに書き込むために使用するライターを設定する必要があります。1秒当たりのフレーム数（fps）を設定し、タイトル、作者、コメントなどのメタデータを追加します。

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
