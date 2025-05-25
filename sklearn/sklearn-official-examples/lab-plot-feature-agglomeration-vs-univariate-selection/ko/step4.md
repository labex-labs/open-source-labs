# 그리드 서치를 사용한 베이지안 릿지 계수 계산

```python
cv = KFold(2)  # 모델 선택을 위한 교차 검증 생성기
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
