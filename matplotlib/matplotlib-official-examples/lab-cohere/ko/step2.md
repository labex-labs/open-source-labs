# 신호 생성

다음으로, 10 Hz 에서 coherent (일관성 있는) 부분을 가지고 무작위 부분도 포함된 두 개의 신호를 생성합니다. 또한 신호에 백색 잡음 (white noise) 을 추가할 것입니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2
```
