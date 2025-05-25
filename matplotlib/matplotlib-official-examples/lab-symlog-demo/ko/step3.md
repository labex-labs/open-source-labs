# 플롯 생성

이제 데이터를 얻었으므로 플롯을 생성할 수 있습니다. 세 개의 서브플롯을 생성하며, 각 서브플롯은 서로 다른 `symlog` 축 스케일링을 갖습니다.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
