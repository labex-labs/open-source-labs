# Figure 및 Subplot 생성

이 단계에서는 figure 와 생성할 각 투영법에 대한 4 개의 subplot 을 생성합니다. `plt.subplots()` 메서드를 사용하여 figure 와 subplot 을 생성합니다.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
