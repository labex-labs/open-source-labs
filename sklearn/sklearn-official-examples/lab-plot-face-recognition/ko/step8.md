# 고유 벡터 시각화

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

입력 데이터에서 추출된 특징을 시각화하기 위해 고유 벡터를 플롯합니다.
