# 막대 차트 생성

다음 단계는 막대 차트를 생성하는 것입니다. `bar()` 함수를 사용하여 차트를 생성합니다. 차트를 위해 두 세트의 막대, 즉 차와 커피에 대한 막대를 생성합니다. 또한 차트에 오차 막대 (error bars) 를 추가합니다.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
