# データセットの読み込み

このステップでは、Scikit-Learn の make_hastie_10_2 関数を使ってデータセットを読み込みます。この関数は、2 値分類用の合成データセットを生成します。

```python
X, y = make_hastie_10_2(n_samples=8000, random_state=42)
```
