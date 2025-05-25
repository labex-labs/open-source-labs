# 범주형 변수를 사용한 플롯

Matplotlib 을 사용하면 범주형 변수를 사용하여 플롯을 생성할 수 있습니다. 범주형 변수를 사용하여 막대 그래프, 산점도, 선 그래프를 만들어 보겠습니다.

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

설명:

- 세 개의 범주형 값을 가진 리스트 `names`와 해당 값을 나타내는 리스트 `values`를 생성합니다.
- `figure` 함수는 지정된 크기의 새 figure 를 생성하기 위해 호출됩니다.
- `subplot` 함수를 사용하여 서브플롯 (subplot) 의 그리드를 생성합니다. 이 예제에서는 막대 그래프, 산점도, 선 그래프와 같이 각기 다른 유형의 플롯을 가진 세 개의 서브플롯을 생성합니다.
- `suptitle` 함수는 figure 의 상위 제목을 설정하는 데 사용됩니다.
