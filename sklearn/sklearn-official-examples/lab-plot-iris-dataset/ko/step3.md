# 데이터 시각화

산점도를 사용하여 아이리스 데이터셋을 시각화합니다. 꽃받침 길이를 꽃받침 너비에 대해 플롯하고, 클래스에 따라 점의 색상을 지정합니다.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# 학습 데이터를 플롯합니다.
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("꽃받침 길이")
plt.ylabel("꽃받침 너비")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
