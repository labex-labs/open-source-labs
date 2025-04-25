# サンプル重みの作成

2 セットのサンプル重みを作成します。最初のセットのサンプル重みはすべてのポイントで一定で、2 番目のセットのサンプル重みは一部のアウトライアーに対して大きくなります。

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
