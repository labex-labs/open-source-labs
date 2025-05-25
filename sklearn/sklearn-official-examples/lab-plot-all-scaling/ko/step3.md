# 분포 정의

데이터를 사전 정의된 범위 내로 가져오기 위해 다양한 스케일러, 변환기 및 정규화기를 리스트에 정의하고, 이를 `distributions`라는 리스트에 저장합니다.

```python
# 분포 정의
distributions = [
    ("스케일링되지 않은 데이터", X),
    ("표준 스케일링 후 데이터", StandardScaler().fit_transform(X)),
    ("최소 - 최대 스케일링 후 데이터", MinMaxScaler().fit_transform(X)),
    ("강건 스케일링 후 데이터", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("샘플별 L2 정규화 후 데이터", Normalizer().fit_transform(X)),
    ("분위수 변환 후 데이터 (균일 pdf)", QuantileTransformer(output_distribution="uniform").fit_transform(X)),
    ("분위수 변환 후 데이터 (가우스 pdf)", QuantileTransformer(output_distribution="normal").fit_transform(X)),
    ("멱 변환 후 데이터 (Yeo-Johnson)", PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("멱 변환 후 데이터 (Box-Cox)", PowerTransformer(method="box-cox").fit_transform(X)),
]
```
