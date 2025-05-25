# 'antialiased' 보간법 (Interpolation) 으로 이미지 업샘플링

마지막으로, 'antialiased' 보간법을 사용하여 이미지를 500 데이터 픽셀에서 530 렌더링된 픽셀로 업샘플링합니다. 이는 더 나은 안티앨리어싱 (antialiasing) 알고리즘을 사용하면 모아레 패턴을 어떻게 줄일 수 있는지 보여줍니다.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
