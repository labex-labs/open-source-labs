# 메뉴 생성

이제 메뉴를 생성할 수 있습니다. 새로운 figure 를 생성하고 왼쪽 여백을 조정합니다. 그런 다음 메뉴 항목 목록을 생성하고 이를 메뉴에 추가합니다. 또한 선택된 항목을 출력하는 각 항목에 대한 콜백 함수를 정의합니다.

```python
fig = plt.figure()
fig.subplots_adjust(left=0.3)
props = ItemProperties(labelcolor='black', bgcolor='yellow',
                       fontsize=15, alpha=0.2)
hoverprops = ItemProperties(labelcolor='white', bgcolor='blue',
                            fontsize=15, alpha=0.2)

menuitems = []
for label in ('open', 'close', 'save', 'save as', 'quit'):
    def on_select(item):
        print('you selected %s' % item.labelstr)
    item = MenuItem(fig, label, props=props, hoverprops=hoverprops,
                    on_select=on_select)
    menuitems.append(item)

menu = Menu(fig, menuitems)
plt.show()
```
