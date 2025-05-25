# 레이블 추가 및 레이아웃 조정

matplotlib.pyplot 의 title, xlabel, ylabel 함수를 사용하여 서브플롯에 제목과 축 레이블을 추가합니다. tight_layout 함수를 사용하여 서브플롯의 레이아웃을 조정합니다.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
