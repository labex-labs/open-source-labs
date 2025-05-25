# 스위스 홀 데이터셋 생성

`make_swiss_roll()` 함수의 `hole=True` 매개변수를 사용하여 스위스 롤 데이터셋에 구멍을 추가하여 스위스 홀 데이터셋을 생성합니다.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
