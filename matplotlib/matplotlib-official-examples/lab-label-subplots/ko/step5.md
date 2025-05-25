# 제목과 함께 레이블 지정

레이블을 제목과 정렬하고 싶다면, 제목에 통합하거나 `loc` 키워드 인수를 사용할 수 있습니다.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
