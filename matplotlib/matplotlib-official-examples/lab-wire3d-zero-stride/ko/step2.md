# figure 와 두 개의 서브플롯 생성

`subplots()` 메서드를 사용하여 figure 와 두 개의 서브플롯을 생성합니다. 또한 서브플롯이 3 차원이 되도록 투영 (projection) 을 `'3d'`로 설정합니다.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
