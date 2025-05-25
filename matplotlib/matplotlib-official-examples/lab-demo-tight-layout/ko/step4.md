# 여러 플롯 생성

동일한 figure 내에서 여러 플롯을 생성할 수도 있습니다.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

여기서는 `subplot` 함수를 사용하여 동일한 figure 내에서 두 개의 플롯을 나란히 생성합니다. `subplot`에 세 개의 인수를 전달합니다: 행 수, 열 수 및 플롯 번호. 그런 다음 각 subplot 에 플롯을 생성합니다.
