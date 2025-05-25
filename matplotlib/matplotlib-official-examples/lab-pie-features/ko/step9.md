# 그림자 수정 (Modify the Shadow)

`pie()` 함수의 `shadow` 매개변수에 인수의 딕셔너리를 전달하여 파이 차트의 그림자를 수정할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
```
