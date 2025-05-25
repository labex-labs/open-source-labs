# 각 열에 대한 서브플롯 생성

`subplots` 인수를 사용하여 각 데이터 열에 대한 개별 서브플롯 (subplot) 을 생성할 수 있습니다.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
