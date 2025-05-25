# PCA 및 커널 PCA 투영 시각화

PCA 와 커널 PCA 투영 결과를 비교하여 차이점을 시각적으로 보여줍니다.

```python
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = plt.subplots(
    ncols=3, figsize=(14, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("테스트 데이터")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("주성분 #1")
pca_proj_ax.set_xlabel("주성분 #0")
pca_proj_ax.set_title("PCA 를 이용한\n테스트 데이터 투영")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("주성분 #1")
kernel_pca_proj_ax.set_xlabel("주성분 #0")
_ = kernel_pca_proj_ax.set_title("커널 PCA 를 이용한\n테스트 데이터 투영")
```
