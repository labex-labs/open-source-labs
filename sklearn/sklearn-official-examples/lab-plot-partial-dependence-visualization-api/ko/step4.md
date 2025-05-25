# 하나의 특징에 대한 부분 의존성 플롯

이 단계에서는 하나의 특징인 "나이"에 대한 부분 의존성 곡선을 같은 축에 그립니다. 이 경우 `tree_disp.axes_`를 두 번째 플롯 함수에 전달합니다.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
