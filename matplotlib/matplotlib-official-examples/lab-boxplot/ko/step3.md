# 기본 박스 플롯 (Box Plot)

데이터를 시각화하기 위해 기본 박스 플롯을 생성하는 것으로 시작합니다. Matplotlib 함수 `boxplot()`을 사용하고 데이터와 레이블을 인수로 전달합니다. 또한 `set_title()` 함수를 사용하여 플롯의 제목을 설정합니다.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
