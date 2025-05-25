# 이미지 재구성

K-평균 모델과 임의 코드북에서 얻은 코드북 및 레이블을 사용하여 압축된 이미지를 재구성합니다.

```python
def recreate_image(codebook, labels, w, h):
    """압축된 이미지를 코드북 및 레이블에서 재구성합니다."""
    return codebook[labels].reshape(w, h, -1)

# 양자화된 이미지와 함께 원본 이미지 표시
plt.figure()
plt.clf()
plt.axis("off")
plt.title("원본 이미지 (96,615 색상)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"양자화된 이미지 ({n_colors} 색상, K-평균)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"양자화된 이미지 ({n_colors} 색상, 임의)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```
