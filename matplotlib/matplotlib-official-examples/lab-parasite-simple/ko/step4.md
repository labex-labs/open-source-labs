# 데이터 추가

`plot` 함수를 사용하여 플롯에 데이터를 추가합니다. 각 선을 변수에 할당하여 나중에 참조할 수 있도록 합니다.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
