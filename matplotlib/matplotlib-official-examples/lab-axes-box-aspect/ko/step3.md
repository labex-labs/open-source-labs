# 정사각형 트윈 축 (Twin Axes)

트윈 축이 있는 정사각형 축을 생성합니다. 트윈 축은 부모의 박스 종횡비 (box aspect) 를 상속받습니다.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```
