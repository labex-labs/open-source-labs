# 색상 맵 생성

이제 클래스 결정 경계를 플롯하기 위한 색상 맵을 생성합니다. 배경에는 밝은 색상을 사용하고 클래스 색상에는 진한 색상을 사용합니다.

```python
h = 0.05  # 메쉬의 단계 크기

# 색상 맵 생성
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
