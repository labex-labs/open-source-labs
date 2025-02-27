# データの読み込み

このステップでは、scikit-learnライブラリからデータを読み込みます。過去の観測データと14の環境変数を持つ2種類の南米の哺乳類のデータを読み込むために、fetch_species_distributions関数を使います。

```python
# Load the compressed data
data = fetch_species_distributions()
```
