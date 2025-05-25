# 복잡한 데이터에서 이상치 탐지

"바나나" 모양의 와인 데이터셋에서 이상치 탐지를 수행합니다. 이전과 같은 세 가지 분류기를 사용하여 결과를 시각화합니다.

```python
# 여러 분류기를 사용하여 이상치 탐지 경계 학습
xx2, yy2 = np.meshgrid(np.linspace(-1, 5.5, 500), np.linspace(-2.5, 19, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(2)
    clf.fit(X2)
    Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
    Z2 = Z2.reshape(xx2.shape)
    plt.contour(
        xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i]
    )

# 결과 플롯 (= 데이터 포인트 클라우드의 모양)
plt.figure(2)  # "바나나" 모양
plt.title("실제 데이터셋 (와인 인식) 에서 이상치 탐지")
plt.scatter(X2[:, 0], X2[:, 1], color="black")
plt.xlim((xx2.min(), xx2.max()))
plt.ylim((yy2.min(), yy2.max()))
plt.ylabel("color_intensity")
plt.xlabel("flavanoids")
plt.show()
```
