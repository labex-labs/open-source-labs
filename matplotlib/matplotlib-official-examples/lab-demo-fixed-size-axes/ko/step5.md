# Figure 에 축 추가

`add_axes()` 함수를 사용하여 figure 에 축을 추가하고, `Divider` 객체의 위치를 전달합니다.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
