# 서브피겨가 있는 그림 만들기

서브피겨가 있는 그림을 만들려면 먼저 `plt.figure()`를 사용하여 그림 객체를 생성해야 합니다. 그런 다음 `fig.subfigures()`를 사용하여 서브피겨를 만들 수 있습니다.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

이렇게 하면 두 개의 서브피겨가 있는 그림이 생성되며, 하나는 다른 하나 위에 위치합니다.
