# Figure 및 Subplot 생성

다음 단계는 figure 와 subplot 을 생성하는 것입니다. `subplots` 함수를 사용하여 나란히 두 개의 subplot 이 있는 figure 를 생성합니다.

```python
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
```
