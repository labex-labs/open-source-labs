# 오프셋 생성

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

세 번째 단계는 Numpy 를 사용하여 오프셋을 생성하는 것입니다. random 함수를 사용하여 오프셋을 생성합니다.
