# 서브플롯 (Subplots) 이 있는 Figure 생성

이제 각 데이터 세트에 대해 하나씩, 네 개의 서브플롯이 있는 Figure 를 생성합니다. 또한 모든 서브플롯에 대해 x 및 y 제한을 동일하게 설정합니다.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
