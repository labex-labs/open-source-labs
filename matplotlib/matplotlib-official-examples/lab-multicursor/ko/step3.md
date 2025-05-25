# 플롯 생성

이제 `plt.subplots` 함수를 사용하여 세 개의 서브플롯을 생성합니다. 두 개의 플롯은 하나의 figure 에 생성되고, 세 번째 플롯은 별도의 figure 에 생성됩니다.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
