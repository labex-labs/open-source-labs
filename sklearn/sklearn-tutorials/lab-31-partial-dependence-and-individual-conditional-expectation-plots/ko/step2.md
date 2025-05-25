# 데이터 로드 및 준비

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# 데이터 조작을 쉽게 하기 위해 DataFrame 생성
df = pd.DataFrame(X, columns=feature_names)
```
