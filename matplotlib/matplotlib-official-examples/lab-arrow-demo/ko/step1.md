# 라이브러리 가져오기 및 함수 정의

첫 번째 단계는 필요한 라이브러리를 가져오고 `make_arrow_graph()` 함수를 정의하는 것입니다. 이 함수는 축 (axes), 데이터, 크기, 표시, 모양, max_arrow_width, arrow_sep, alpha, normalize_data, ec, labelcolor 및 kwargs 와 같은 다양한 매개변수를 입력으로 받습니다. 이 매개변수를 사용하여 화살표 플롯을 생성합니다.

```python
# Import libraries
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max_arrow_width : float
        Maximum width of an arrow, in data coordinates.
    arrow_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    **kwargs
        `.FancyArrow` properties, e.g. *linewidth* or *edgecolor*.
    """

    # code block
```
