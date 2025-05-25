# 서브피겨에 데이터 플롯하기

서브피겨에 데이터를 플롯하려면 `subfig.subplots()`를 사용하여 각 서브피겨에 대한 서브플롯을 생성해야 합니다. 그런 다음 Matplotlib 의 모든 플롯 함수를 사용하여 플롯을 만들 수 있습니다.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

이렇게 하면 각 서브피겨에 임의 데이터의 플롯이 있는 두 개의 서브피겨가 생성됩니다.
