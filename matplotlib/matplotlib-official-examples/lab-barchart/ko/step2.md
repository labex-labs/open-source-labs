# 데이터 준비

다음으로, 차트에 사용할 데이터를 준비합니다. 펭귄 종 3 가지와 속성 3 가지가 있으므로, 종별 각 속성의 평균값을 가진 딕셔너리를 생성합니다.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
