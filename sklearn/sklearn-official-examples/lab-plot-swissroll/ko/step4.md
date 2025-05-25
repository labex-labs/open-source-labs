# 스위스 롤 데이터셋의 LLE 및 t-SNE 임베딩 시각화

다양한 색상으로 서로 다른 점을 표현하는 산점도를 사용하여 스위스 롤 데이터셋의 LLE 및 t-SNE 임베딩을 시각화할 수 있습니다.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("LLE 임베딩 (Swiss Roll)")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("t-SNE 임베딩 (Swiss Roll)")
```
