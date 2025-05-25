# 매개변수 정의

이 단계에서는 아이리스 데이터셋에서 결정 경계를 시각화하는 데 필요한 매개변수를 정의합니다.

```python
# 매개변수
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # 결정 경계 윤곽선을 위한 미세 단계 너비
plot_step_coarser = 0.5  # 거친 분류기 추측을 위한 단계 너비
RANDOM_SEED = 13  # 각 반복에서 시드를 고정
```
