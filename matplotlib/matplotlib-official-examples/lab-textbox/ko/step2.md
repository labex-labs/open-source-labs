# 초기 플롯 생성

다음으로, 사용자의 입력에 따라 업데이트될 초기 플롯을 생성합니다. 이 예제에서는 독립 변수 `t`를 사용하여 함수의 플롯을 생성합니다.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
