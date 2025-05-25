# 간단한 플롯 생성

시작하기 위해, `pyplot`의 `plot` 함수를 사용하여 간단한 플롯을 생성해 보겠습니다. 이 예제에서는 y 값 `[1, 2, 3, 4]`를 가진 선 그래프를 플롯합니다.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

설명:

- `matplotlib`에서 `pyplot` 모듈을 가져와 `plt`로 별칭을 지정합니다.
- `plot` 함수는 선 그래프를 생성하는 데 사용됩니다. y 값의 단일 리스트를 제공하면, Python 범위가 0 부터 시작하므로 x 값은 자동으로 `[0, 1, 2, 3]`으로 생성됩니다.
- `ylabel` 함수는 y 축의 레이블을 설정합니다.
- 마지막으로, `show` 함수는 플롯을 표시합니다.
