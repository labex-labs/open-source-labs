# 재귀 규칙 설정

5 번째 부활절마다 사용자 정의 날짜 눈금을 설정할 것입니다. 이를 위해 `rrulewrapper` 함수를 사용하여 재귀 규칙을 설정해야 합니다.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```
