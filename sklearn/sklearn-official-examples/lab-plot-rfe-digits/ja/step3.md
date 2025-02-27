# 特徴のランキング付け

RFE オブジェクトにデータを適合させた後、重要度に基づいて特徴をランキング付けすることができます。RFE オブジェクトの `ranking_` 属性を使って特徴のランキングを取得します。また、ランキングを元の画像の形状に合わせるために整形します。

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
