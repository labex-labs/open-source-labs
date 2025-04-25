# FastICA アルゴリズムの使用

このステップでは、FastICA アルゴリズムを使用します。このアルゴリズムは、非ガウス性の高い射影に対応する特徴空間内の方向を見つけます。

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)
```
