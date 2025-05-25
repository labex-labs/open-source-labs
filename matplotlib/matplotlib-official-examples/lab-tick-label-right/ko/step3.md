# 샘플 플롯 생성

y 축 눈금 레이블이 오른쪽에 있는 경우의 모양을 확인하기 위해 샘플 플롯을 생성해 보겠습니다.

```python
x = np.arange(10)

fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax0.plot(x)
ax0.yaxis.tick_left()

ax1.plot(x)

plt.show()
```
