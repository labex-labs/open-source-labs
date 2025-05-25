# 차트 사용자 정의

레이블, 제목을 추가하고 x 축 눈금 레이블과 범례를 조정하여 차트를 사용자 정의할 수 있습니다. 또한 모든 데이터가 보이도록 y 축 제한을 설정합니다.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
