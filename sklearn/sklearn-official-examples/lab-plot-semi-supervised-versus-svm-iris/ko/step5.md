# 결정 경계 시각화

입력 특징 공간을 커버하는 메쉬 그리드를 생성하고 각 분류기를 사용하여 메쉬 그리드의 점에 대한 레이블을 예측합니다. 그런 다음 결정 경계와 레이블이 지정된 데이터 점을 플롯합니다.

```python
# 플롯을 위한 메쉬 그리드 생성
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 레이블에 대한 색상 맵 정의
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}

# 분류기 설정
classifiers = (ls30, st30, ls50, st50, ls100, rbf_svc)

# 각 분류기의 결정 경계와 레이블이 지정된 데이터 점 플롯
for i, (clf, y_train, title) in enumerate(classifiers):
    # 결정 경계 플롯
    plt.subplot(3, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 결과를 색상 플롯에 넣기
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis("off")

    # 레이블이 지정된 데이터 점 플롯
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, edgecolors="black")

    plt.title(title)

plt.suptitle("레이블이 지정되지 않은 점은 흰색으로 표시됨", y=0.1)
plt.show()
```
