# 서브플롯 생성

`subplots()` 함수를 사용하여 2x3 그리드의 서브플롯을 생성합니다.

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
