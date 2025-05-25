# Figure 및 외부 GridSpec 생성

다음 단계는 figure 와 외부 gridspec 을 생성하는 것입니다. 이 예제에서는 1x2 gridspec 을 생성합니다.

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```
