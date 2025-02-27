# GridSearchを用いたBayesian Ridgeの係数の計算

```python
cv = KFold(2)  # モデル選択のための交差検証ジェネレータ
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
