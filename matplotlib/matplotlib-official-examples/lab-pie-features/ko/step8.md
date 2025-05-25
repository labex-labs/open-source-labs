# 크기 제어

`pie()` 함수의 `radius` 매개변수를 설정하여 파이 차트의 크기를 제어할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=0.5)
```
