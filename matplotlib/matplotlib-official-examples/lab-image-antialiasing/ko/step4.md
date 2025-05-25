# 'nearest' 보간법 (Interpolation) 으로 이미지 업샘플링

이제 'nearest' 보간법을 사용하여 이미지를 500 데이터 픽셀에서 530 렌더링된 픽셀로 업샘플링합니다. 이는 업샘플링 비율이 정수가 아닌 경우 이미지가 업샘플링될 때에도 모아레 패턴이 어떻게 발생할 수 있는지 보여줍니다.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
