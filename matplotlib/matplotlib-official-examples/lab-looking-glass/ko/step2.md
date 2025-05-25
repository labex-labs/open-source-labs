# 랜덤 데이터 생성

NumPy 를 사용하여 두 세트의 랜덤 데이터를 생성합니다. 이 데이터는 산점도를 만들기 위해 플롯됩니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```
