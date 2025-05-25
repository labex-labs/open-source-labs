# 서브피겨 사용자 정의

Matplotlib 에서 제공하는 다양한 함수를 사용하여 서브피겨를 사용자 정의할 수 있습니다. 예를 들어, `set_title()` 및 `set_xlabel()`/`set_ylabel()`을 사용하여 제목과 축 레이블을 설정할 수 있습니다.

```python
ax1.set_title('Subfigure 1')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')

ax2.set_title('Subfigure 2')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
```

이렇게 하면 각 서브피겨에 대한 제목과 축 레이블이 설정됩니다.
