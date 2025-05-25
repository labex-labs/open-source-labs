# 특징 선택 및 매핑 정의

다음으로, 시각화를 용이하게 하기 위해 데이터셋에서 두 개의 특징을 선택하고, 더 나은 시각화를 위해 특징 이름의 매핑을 정의합니다.

```python
# 두 개의 특징 선택
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# 특징 매핑 정의
feature_mapping = {
    "MedInc": "블록별 중간 소득",
    "AveOccup": "평균 주택 점유율",
}
```
