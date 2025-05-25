# 슬라이스 분리 (Explode)

`pie()` 함수의 `explode` 매개변수에 값 리스트를 전달하여 파이 차트의 하나 이상의 슬라이스를 분리 (explode) 할 수 있습니다.

```python
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
