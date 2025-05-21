# 더 복잡한 패턴 처리

현재 함수는 camelCase 에 대해 작동하지만, 다음과 같은 추가 패턴을 처리하도록 개선해야 합니다:

1.  PascalCase (예: `HelloWorld`)
2.  하이픈이 있는 문자열 (예: `hello-world`)
3.  이미 밑줄이 있는 문자열 (예: `hello_world`)

이러한 경우를 처리하도록 함수를 업데이트해 보겠습니다:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

우리가 한 개선 사항:

1.  먼저 하이픈을 공백으로 바꿉니다.
2.  새로운 정규 표현식 `re.sub('([A-Z]+)', r' \1', s)`는 PascalCase 에 도움이 되도록 대문자 시퀀스 앞에 공백을 추가합니다.
3.  camelCase 처리 정규 표현식을 유지합니다.
4.  마지막으로, 문자열을 공백으로 분할하고, 밑줄로 결합하고, 소문자로 변환하여 남아있는 공백을 처리하고 일관된 출력을 보장합니다.

스크립트를 실행하여 다양한 입력 형식으로 테스트하십시오:

```bash
python3 ~/project/snake_case.py
```

다음과 같은 출력이 표시되어야 합니다:

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

이제 함수가 더 강력해졌으며 다양한 입력 형식을 처리할 수 있습니다. 다음 단계에서는 최종 개선 사항을 적용하고 전체 테스트 스위트에 대해 테스트할 것입니다.
