# 숫자 정규화 함수 정의

모든 숫자 토큰을 플레이스홀더로 매핑하는 함수 `number_normalizer()`를 정의합니다. 이는 차원 축소에 사용됩니다.

```python
def number_normalizer(tokens):
    """모든 숫자 토큰을 플레이스홀더로 매핑합니다.

    많은 응용 프로그램에서 숫자로 시작하는 토큰은 직접적으로 유용하지 않지만, 그러한 토큰이 존재한다는 사실은 관련성이 있을 수 있습니다. 이러한 형태의 차원 축소를 적용하면 일부 방법이 더 나은 성능을 보일 수 있습니다.
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```
