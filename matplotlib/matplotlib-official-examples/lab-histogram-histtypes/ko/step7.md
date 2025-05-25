# 스택 막대 (stacked bars) 를 가진 두 개의 히스토그램 생성

`hist` 함수를 두 번 호출하고 `histtype` 매개변수를 `'barstacked'`로 설정하여 스택 막대 (stacked bars) 를 가진 두 개의 히스토그램을 생성할 수 있습니다. 이 예제에서는 스택 막대 (stacked bars) 를 가진 두 개의 히스토그램을 생성합니다.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
