# テキストデータの読み込み

まず、扱うテキストデータを読み込む必要があります。20 個の異なるトピックのニュース記事が含まれる 20 Newsgroups データセットを使用します。データセットを読み込むには、scikit-learn の `fetch_20newsgroups` 関数を使用できます。

```python
from sklearn.datasets import fetch_20newsgroups

# データセットを読み込む
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

これでデータが読み込まれました。そして、その構造と内容を調べることができます。
