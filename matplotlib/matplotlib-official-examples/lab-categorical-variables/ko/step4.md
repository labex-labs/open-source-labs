# 산점도 (Scatter Plot)

두 개의 범주형 변수 간의 관계를 표시하기 위해 산점도를 생성할 수도 있습니다. 이 경우, 동일한 과일 데이터를 사용하고 개수에 약간의 무작위 노이즈 (random noise) 를 추가하여 두 번째 변수를 생성합니다.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
