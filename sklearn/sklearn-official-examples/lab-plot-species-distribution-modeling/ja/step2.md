# データの読み込み

このステップでは、scikit-learn ライブラリからデータを読み込みます。過去の観測データと 14 の環境変数を持つ 2 種類の南米の哺乳類のデータを読み込むために、fetch_species_distributions 関数を使います。

```python
# Load the compressed data
data = fetch_species_distributions()
```
