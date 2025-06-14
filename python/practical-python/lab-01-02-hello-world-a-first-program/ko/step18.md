# 연습 1.5: 튕기는 공

고무공이 100 미터 높이에서 떨어지고, 땅에 닿을 때마다 떨어진 높이의 3/5 만큼 다시 튕겨 올라갑니다. 처음 10 번의 튕김 높이를 보여주는 표를 출력하는 프로그램 `bounce.py`를 작성하십시오.

다음은 해결책입니다.

```python
# bounce.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
```

프로그램은 다음과 유사한 표를 만들어야 합니다.

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

_참고: round() 함수를 사용하면 출력을 약간 정리할 수 있습니다. 출력을 소수점 4 자리로 반올림하는 데 사용해 보십시오._

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```
