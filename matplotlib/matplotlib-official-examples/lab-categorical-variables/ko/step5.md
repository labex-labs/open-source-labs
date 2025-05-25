# 선 그래프 (Line Plot)

선 그래프는 범주형 변수가 시간에 따라 어떻게 변화하는지 보여주는 데 사용될 수 있습니다. 이 예제에서는 다양한 활동 동안 고양이와 개의 행복 수준에 대한 데이터를 사용합니다.

```python
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
plt.plot(activity, dog, label="dog")
plt.plot(activity, cat, label="cat")
plt.title('Happiness Levels')
plt.xlabel('Activity')
plt.ylabel('Happiness')
plt.legend()
plt.show()
```
