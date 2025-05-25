# 서브피겨 생성 및 `test_rotation_mode` 함수 호출

두 개의 서브피겨를 생성하고 `fig` 및 `mode` 매개변수를 사용하여 `test_rotation_mode` 함수를 호출합니다.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
