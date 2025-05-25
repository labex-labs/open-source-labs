# 파이프라인 검사

모델을 더 잘 이해하기 위해 파이프라인을 검사할 수 있습니다. 선택된 특징의 인덱스를 사용하여 원래 특징 이름을 검색할 수 있습니다.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
