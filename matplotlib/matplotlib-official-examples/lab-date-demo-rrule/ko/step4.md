# 눈금 로케이터 및 포맷터 설정

이전 단계에서 설정한 재귀 규칙을 기반으로 눈금 로케이터를 설정하기 위해 `RRuleLocator` 함수를 사용합니다. 또한 눈금 포맷터를 설정하기 위해 `DateFormatter` 함수를 사용합니다.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```
