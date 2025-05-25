# 데이터 플롯 및 x 축 눈금 설정

마지막으로, `plot` 함수를 사용하여 데이터를 플롯하고, 앞서 설정한 눈금 로케이터 및 포맷터 함수를 사용하여 x 축 눈금을 설정할 수 있습니다.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
