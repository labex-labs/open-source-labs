# 스위스 홀 데이터셋의 LLE 및 t-SNE 임베딩 시각화

스위스 홀 데이터셋의 LLE 및 t-SNE 임베딩을 산점도로 시각화하여 서로 다른 점을 다른 색상으로 표현할 수 있습니다.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("스위스 홀의 LLE 임베딩")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("스위스 홀의 t-SNE 임베딩")
```
