# 서브플롯 생성

Matplotlib 에서 서브플롯을 생성하려면 `subplot()` 메서드를 사용할 수 있습니다. 이 메서드는 세 개의 인수를 받습니다: 행의 수, 열의 수, 그리고 플롯 번호입니다. 다음은 세 개의 서브플롯을 생성하는 예입니다.

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
