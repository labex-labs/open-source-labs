# Figure 1 생성

먼저 두 개의 subplot 을 포함할 첫 번째 figure 를 생성합니다. 첫 번째 사인파는 상단 subplot 에, 첫 번째 사인파의 진폭의 두 배는 하단 subplot 에 플롯합니다.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s1)

# Bottom subplot
plt.subplot(212)
plt.plot(t, 2*s1)
```
