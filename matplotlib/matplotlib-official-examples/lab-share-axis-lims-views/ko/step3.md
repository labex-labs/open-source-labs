# 첫 번째 플롯 생성

이제 `subplot`을 사용하여 첫 번째 플롯을 생성해 보겠습니다. `subplot`은 세 개의 인수를 받습니다: 행의 수, 열의 수, 그리고 플롯 번호입니다. 이 예제에서는 2 개의 행과 1 개의 열을 가진 플롯 (`211`) 을 생성할 것이며, 이는 첫 번째 플롯이 상단 행에 위치함을 의미합니다.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```
