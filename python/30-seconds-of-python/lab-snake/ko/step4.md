# 최종 구현 및 테스트

이제 모든 필요한 경우를 처리하고 모든 테스트 케이스를 통과하는지 확인하기 위해 구현을 완료해 보겠습니다.

`snake_case.py` 파일을 최종 구현으로 업데이트하십시오:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern
    s = re.sub('([A-Z][a-z]+)', r' \1', s)

    # Handle sequences of uppercase letters
    s = re.sub('([A-Z]+)', r' \1', s)

    # Split by whitespace and join with underscores
    return '_'.join(s.split()).lower()

# Test with a complex example
if __name__ == "__main__":
    test_string = "some-mixed_string With spaces_underscores-and-hyphens"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

이 최종 구현은 다음과 같습니다:

1.  하이픈을 공백으로 바꿉니다.
2.  `re.sub('([A-Z][a-z]+)', r' \1', s)`를 사용하여 "Word"와 같은 패턴 앞에 공백을 추가합니다.
3.  `re.sub('([A-Z]+)', r' \1', s)`를 사용하여 대문자 시퀀스 앞에 공백을 추가합니다.
4.  공백으로 분할하고, 밑줄로 결합하고, 소문자로 변환합니다.

이제 설정 단계에서 생성된 테스트 스위트에 대해 함수를 실행해 보겠습니다:

```bash
python3 ~/project/test_snake.py
```

구현이 올바르면 다음을 볼 수 있습니다:

```
All tests passed! Your snake case function works correctly.
```

축하합니다! 다양한 입력 형식을 처리할 수 있는 강력한 snake case 변환 함수를 성공적으로 구현했습니다.

함수가 원래 문제의 예제를 사용하여 사양을 정확하게 따르는지 확인해 보겠습니다:

```python
# Add this to the end of your snake_case.py file:
if __name__ == "__main__":
    examples = [
        'camelCase',
        'some text',
        'some-mixed_string With spaces_underscores-and-hyphens',
        'AllThe-small Things'
    ]

    for ex in examples:
        result = snake(ex)
        print(f"Original: {ex}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

업데이트된 스크립트를 실행하십시오:

```bash
python3 ~/project/snake_case.py
```

모든 예제가 snake case 로 올바르게 변환되는 것을 볼 수 있습니다:

```
Original: some-mixed_string With spaces_underscores-and-hyphens
Snake case: some_mixed_string_with_spaces_underscores_and_hyphens
Original: camelCase
Snake case: camel_case
--------------------
Original: some text
Snake case: some_text
--------------------
Original: some-mixed_string With spaces_underscores-and-hyphens
Snake case: some_mixed_string_with_spaces_underscores_and_hyphens
--------------------
Original: AllThe-small Things
Snake case: all_the_small_things
--------------------
```
