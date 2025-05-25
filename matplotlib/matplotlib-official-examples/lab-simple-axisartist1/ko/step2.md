# Figure 및 Subplot 생성

`add_gridspec` 메서드를 사용하여 두 개의 subplot 이 있는 figure 를 생성합니다.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```
