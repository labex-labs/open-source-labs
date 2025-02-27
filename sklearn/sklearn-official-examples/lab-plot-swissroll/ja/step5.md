# スイスホールデータセットの生成

`make_swiss_roll()` 関数の `hole=True` パラメータを使って、スイスロールデータセットに穴を追加することで、スイスホールデータセットを生成します。

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
