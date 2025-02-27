# ランダムなコードブックを使って色インデックスを予測する

ランダムなコードブックを使って画像全体の色インデックスを予測します。

```python
# ランダムなコードブックを取得する
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# ランダムなコードブックを使って画像全体の色インデックスを予測する
print("Predicting color indices on the full image (random)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"done in {time() - t0:0.3f}s.")
```

なお、`pairwise_distances_argmin` は既存の関数ですが、コード内に定義されていないため、そのまま残しておきます。もしこの関数が定義されていない場合、コードはエラーを起こします。
