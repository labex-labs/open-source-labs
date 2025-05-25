# 정사영 투영 설정

첫 번째 서브플롯이 0 도의 `FOV` (시야각) 와 무한대의 `focal_length` (초점 거리) 를 사용하여 정사영 투영을 사용하도록 설정합니다.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
