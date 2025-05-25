# 서브플롯 생성

이제 `subplots` 함수를 사용하여 서브플롯을 생성합니다. 동일한 종횡비 (aspect ratio) 를 가진 서브플롯 그리드를 생성하고, x 축과 y 축에서 눈금을 제거합니다. 또한 정렬을 시각화하기 위해 각 서브플롯의 중앙에 수직 및 수평선을 추가합니다.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
