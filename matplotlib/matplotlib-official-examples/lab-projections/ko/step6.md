# 원근 투영 설정

두 번째 서브플롯이 기본 `FOV` (시야각) 90 도와 `focal_length` (초점 거리) 1 을 사용하여 원근 투영을 사용하도록 설정합니다.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

세 번째 서브플롯이 `FOV` 157.4 도와 `focal_length` 0.2 를 사용하여 원근 투영을 사용하도록 설정합니다.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
