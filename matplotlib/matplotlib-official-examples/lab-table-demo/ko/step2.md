# 데이터셋 생성

다음으로, 연도별로 다양한 자연 재해로 인해 발생한 손실을 시각화하기 위한 샘플 데이터셋을 생성합니다. 데이터를 저장하기 위해 2 차원 리스트를 사용하고, 열 이름을 저장하기 위해 튜플을 사용합니다.

```python
data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
```
