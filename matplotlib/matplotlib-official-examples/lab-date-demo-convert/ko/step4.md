# 그래프 생성

이제 날짜와 y 값을 사용하여 그래프를 생성할 수 있습니다. 먼저 subplots 함수를 사용하여 figure 및 axis 객체를 생성합니다. 그런 다음 plot 함수를 사용하여 그래프를 그립니다. 다음 코드를 복사하여 붙여넣으십시오:

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
