# Z 축 사용자 정의

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

`set_zlim()` 함수를 사용하여 z 축을 사용자 정의하여 z 축의 범위를 -1.01 에서 1.01 로 설정합니다. 그런 다음 `set_major_locator()` 함수를 사용하여 `LinearLocator(10)`을 사용하여 z 축의 눈금 수를 10 으로 설정합니다. 마지막으로, `set_major_formatter()` 함수를 사용하여 `StrMethodFormatter`를 사용하여 z 축 눈금 레이블의 형식을 지정합니다.
