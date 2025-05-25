# 대화형으로 다각형 생성

대화형으로 다각형을 생성하려면 `Figure` 객체와 `Axes` 객체를 생성해야 합니다. 그런 다음, 플롯을 클릭하여 `PolygonSelector` 객체를 생성하고 정점을 추가할 수 있습니다. 또한 `shift` 및 `ctrl` 키를 사용하여 정점을 이동할 수 있습니다.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("다각형을 생성하려면 그림을 클릭하십시오.")
print("'esc' 키를 눌러 새 다각형을 시작하십시오.")
print("모든 정점을 이동하려면 'shift' 키를 누르고 시도하십시오.")
print("단일 정점을 이동하려면 'ctrl' 키를 누르고 시도하십시오.")

plt.show()
```
