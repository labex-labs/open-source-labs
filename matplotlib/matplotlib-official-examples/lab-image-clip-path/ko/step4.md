# 패치 생성

패치를 생성하기 위해 Matplotlib 의 `patches` 모듈을 사용합니다. (260, 200) 지점을 중심으로 하고 반지름이 200 픽셀인 원형 패치를 생성합니다.

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
