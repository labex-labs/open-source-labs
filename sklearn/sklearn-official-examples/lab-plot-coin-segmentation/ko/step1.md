# 이미지 로드 및 전처리

그리스 동전 이미지를 로드하고, 처리하기 쉽도록 전처리하는 것으로 시작합니다. 이미지 크기를 원본 크기의 20% 로 조정하고, 다운샘플링 전에 가우시안 필터를 적용하여 앨리어싱 아티팩트를 줄여 부드럽게 합니다.

```python
# 동전 이미지를 NumPy 배열로 로드
orig_coins = coins()

# 처리 속도를 높이기 위해 원본 크기의 20% 로 크기 조정
# 다운샘플링 전에 가우시안 필터를 적용하여 부드럽게 함으로써
# 앨리어싱 아티팩트를 줄입니다.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
