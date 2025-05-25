# 샘플 데이터 생성

이제 `numpy`를 사용하여 플롯할 샘플 데이터를 생성합니다.

```python
# 재현성을 위해 난수 상태 고정
np.random.seed(19680801)

x = np.arange(0.0, 5.0, 0.01)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.randn(len(x))
```
