# 첫 번째 해칭 패턴 세트 생성

다음 목록을 사용하여 첫 번째 해칭 패턴 세트를 생성합니다.

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

그런 다음 루프를 사용하여 각 해칭 패턴으로 사각형을 생성하고 이를 서브플롯에 추가합니다.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
