# 학습 데이터 포인트 플롯

이제 결정 경계 위에 학습 데이터 포인트를 플롯합니다. 서로 다른 대상 값에 대해 서로 다른 색상으로 학습 데이터 포인트를 플롯하기 위해 scatter() 메서드를 사용합니다.

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("다중 클래스 SGD 의 결정 경계")
plt.axis("tight")
```
