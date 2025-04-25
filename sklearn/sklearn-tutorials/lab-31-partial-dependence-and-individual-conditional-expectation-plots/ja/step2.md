# データを読み込んで準備する

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# データ操作を簡単にするために DataFrame を作成する
df = pd.DataFrame(X, columns=feature_names)
```
