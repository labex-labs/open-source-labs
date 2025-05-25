# 플롯 생성

이제 플롯을 생성할 준비가 되었습니다. Matplotlib 의 `plot` 함수를 사용하여 동일한 그래프에 세 개의 선을 플롯하며, 각 선에는 미리 정의된 레이블이 있습니다. `label` 매개변수를 사용하여 각 선에 레이블을 할당합니다.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
