# 3D 플롯 생성

4 단계에서 정의된 레이아웃을 기반으로 `subplot_mosaic`를 사용하여 3D 플롯을 생성합니다.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
