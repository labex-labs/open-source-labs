# ROC 곡선 그리기

다음으로 `RocCurveDisplay.from_estimator` 함수를 사용하여 ROC 곡선을 그립니다. 이 함수는 학습된 분류기, 테스트 데이터셋, 실제 레이블을 입력으로 받아 ROC 곡선을 그릴 수 있는 객체를 반환합니다. 그런 다음 `show()` 메서드를 호출하여 플롯을 표시합니다.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
