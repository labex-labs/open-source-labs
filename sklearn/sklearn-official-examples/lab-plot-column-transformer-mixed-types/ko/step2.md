# 데이터셋 로드

이 단계에서는 `fetch_openml`를 사용하여 OpenML 의 타이타닉 데이터셋을 로드합니다.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
