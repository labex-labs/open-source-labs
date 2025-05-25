# 서브플롯 생성

`plt.subplot()` 메서드를 사용하여 서브플롯을 생성할 수 있습니다. 이 예제에서는 첫 번째 서브플롯이 첫 번째 행과 세 개의 열을 모두 차지하고, 두 번째 및 세 번째 서브플롯이 각각 두 번째 및 세 번째 행을 차지하며, 첫 번째 서브플롯과 x 축을 공유하는 세 개의 서브플롯을 생성합니다.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
