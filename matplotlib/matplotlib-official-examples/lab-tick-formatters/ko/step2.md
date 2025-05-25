# 간단한 서식 지정

이 단계에서는 문자열 또는 함수를 `~.Axis.set_major_formatter` 또는 `~.Axis.set_minor_formatter`에 전달하여 간단한 포맷터 (formatter) 를 사용하는 방법을 보여줍니다. 문자열 포맷터와 함수 포맷터를 사용하는 두 개의 플롯을 생성합니다.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# A ``str``, using format string function syntax, can be used directly as a
# formatter.  The variable ``x`` is the tick value and the variable ``pos`` is
# tick position.  This creates a StrMethodFormatter automatically.
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# A function can also be used directly as a formatter. The function must take
# two arguments: ``x`` for the tick value and ``pos`` for the tick position,
# and must return a ``str``. This creates a FuncFormatter automatically.
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
