# アウトライアスコアを取得する

アウトライアを予測するだけでなく、`negative_outlier_factor_`属性を使用して各観測値のアウトライアスコアにもアクセスできます。低いアウトライアスコアは、より高い異常性を示します。

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
