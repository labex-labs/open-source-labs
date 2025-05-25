# RBF 커널 SVM 및 선형 SVM 의 결정 경계

```python
# 데이터의 첫 두 주요 구성 요소로 투영하여 결정 경계를 시각화합니다.
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# 첫 두 주요 구성 요소에 따라 그리드를 생성합니다.
multiples = np.arange(-2, 2, 0.1)
# 첫 번째 구성 요소에 따른 단계
first = multiples[:, np.newaxis] * pca.components_[0, :]
# 두 번째 구성 요소에 따른 단계
second = multiples[:, np.newaxis] * pca.components_[1, :]
# 결합
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# 플롯 제목
titles = [
    "rbf 커널을 사용한 SVC",
    "SVC (선형 커널)\nFourier rbf 특징 맵\nn_components=100",
    "SVC (선형 커널)\nNystroem rbf 특징 맵\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# 예측 및 플롯
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # 결정 경계를 플롯합니다. 이를 위해 메쉬 [x_min, x_max]x[y_min, y_max] 의 각 점에 색상을 할당합니다.
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # 결과를 색상 플롯에 넣습니다.
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # 계산된 등고선 레벨에서 색상으로의 매핑을 조정합니다.
    plt.contourf(
        multiples,
        multiples,
        Z,
        levels=levels - lv_eps,
        cmap=plt.cm.tab10,
        vmin=0,
        vmax=10,
        alpha=0.7,
    )
    plt.axis("off")

    # 훈련 점도 플롯합니다.
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=targets_train,
        cmap=plt.cm.tab10,
        edgecolors=(0, 0, 0),
        vmin=0,
        vmax=10,
    )

    plt.title(titles[i])
plt.tight_layout()
plt.show()
```
