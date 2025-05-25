# 플롯 생성

이제 데이터를 갖추었으므로 Matplotlib 을 사용하여 플롯을 생성할 수 있습니다. 이 예제에서는 plot() 함수를 사용하여 산점도 (scatter plot) 를 생성합니다.

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
