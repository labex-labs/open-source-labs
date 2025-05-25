# 임의 코드북을 사용한 색상 인덱스 예측

전체 이미지에 대한 색상 인덱스를 임의 코드북을 사용하여 예측합니다.

```python
# 임의 코드북 가져오기
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# 임의 코드북을 사용하여 전체 이미지에 대한 색상 인덱스 예측
print("전체 이미지에 대한 색상 인덱스 예측 (임의)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"done in {time() - t0:0.3f}s.")
```
