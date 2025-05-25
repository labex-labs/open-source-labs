# IPCA 수행

IPCA 클래스의 인스턴스를 초기화하고 데이터에 맞춰 적용하여 아이리스 데이터셋에 IPCA 를 수행합니다.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
