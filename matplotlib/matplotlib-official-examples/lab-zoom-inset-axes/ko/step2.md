# 플롯 생성

다음으로, 샘플 데이터를 사용하여 플롯을 생성합니다. 데이터 소스로 이변량 정규 분포 (bivariate normal distribution) 를 사용합니다.

```python
fig, ax = plt.subplots()

# make data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z
extent = (-3, 4, -4, 3)

ax.imshow(Z2, extent=extent, origin="lower")
```
