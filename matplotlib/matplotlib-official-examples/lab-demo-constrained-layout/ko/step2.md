# 예시 플롯 정의

x 및 y 레이블과 제목이 있는 간단한 선 플롯을 생성하는 함수를 정의합니다.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
