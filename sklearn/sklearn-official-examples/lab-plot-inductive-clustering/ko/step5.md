# 알 수 없는 인스턴스에 대한 클러스터 멤버십 예측

이 단계에서는 생성된 새로운 샘플에 대한 클러스터 멤버십을 예측하기 위해 귀납적 학습 모델을 사용합니다. `InductiveClusterer` 클래스의 `predict` 함수를 사용하고 새로운 샘플과 그 가능한 클러스터를 플롯합니다.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("알 수 없는 인스턴스 분류")
```
