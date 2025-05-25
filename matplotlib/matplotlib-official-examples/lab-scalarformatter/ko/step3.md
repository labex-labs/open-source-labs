# 예제 플롯용 서브플롯 생성

예제 플롯을 표시하기 위해 3 x 3 그리드의 서브플롯을 생성합니다.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
