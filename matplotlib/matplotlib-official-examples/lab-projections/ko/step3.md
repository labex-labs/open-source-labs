# 서브플롯이 있는 Figure 생성

`plt.subplots`를 사용하여 세 개의 서브플롯이 있는 figure 를 생성합니다.

```python
fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})
```
