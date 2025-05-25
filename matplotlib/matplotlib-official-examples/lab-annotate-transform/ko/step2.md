# 데이터 생성

다음으로, 플롯할 데이터를 생성합니다. 사인파 (sine wave) 를 생성하기 위해 `numpy` 라이브러리를 사용합니다.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
