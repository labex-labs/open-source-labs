# 특징 선택 비교 플롯

각 특징의 특징 점수와 가중치를 플롯하여 단변량 특징 선택의 영향을 시각적으로 확인할 수 있습니다.

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"단변량 점수 ($-Log(p_{value})$)"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="SVM 가중치")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="선택 후 SVM 가중치",
)

plt.title("특징 선택 비교")
plt.xlabel("특징 번호")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```
