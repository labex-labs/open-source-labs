# 사전 학습

사전 학습은 입력 데이터를 간단한 요소들의 조합으로 표현하는 희소 표현을 찾는 방법입니다. 이러한 간단한 요소들은 사전을 구성합니다. 대용량 데이터 세트에 더 적합한 DictionaryLearning 의 빠른 버전인 MiniBatchDictionaryLearning 을 적용합니다.

```python
# 사전 학습
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("사전 학습", batch_dict_estimator.components_[:n_components])
```
