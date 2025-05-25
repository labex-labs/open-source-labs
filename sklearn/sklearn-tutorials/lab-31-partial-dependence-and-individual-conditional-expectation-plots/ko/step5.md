# 개별 조건부 기댓값 플롯 생성 및 시각화

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# 그림 크기 및 제목 설정
fig.set_size_inches(10, 8)
fig.suptitle('개별 조건부 기댓값 플롯')

plt.show()
```
