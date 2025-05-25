# LabelSpreading 모델 학습 및 평가

이 단계에서는 레이블이 지정된 데이터의 20% 에 대해 LabelSpreading 을 사용합니다. 레이블이 지정된 데이터의 20% 를 무작위로 선택하고, 해당 데이터로 모델을 학습한 다음, 나머지 레이블이 지정되지 않은 데이터에 대한 레이블을 예측하는 데 모델을 사용합니다.

```python
# LabelSpreading 파이프라인 학습 및 평가
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "테스트 세트에서의 마이크로 평균 F1 점수: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
