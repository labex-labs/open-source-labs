# 디자인 모범 사례 (Design Best Practices)

함수 인자 (function arguments) 에는 항상 짧지만 의미 있는 이름을 부여하십시오.

함수를 사용하는 사람은 키워드 호출 스타일 (keyword calling style) 을 사용하고 싶을 수 있습니다.

```python
d = read_prices('prices.csv', debug=True)
```

Python 개발 도구는 도움말 기능 및 문서에서 이름을 표시합니다.
