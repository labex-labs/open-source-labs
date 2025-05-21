# 정규 표현식 (Regular Expressions) 을 사용한 패턴 매칭

문자열을 snake case 로 변환하기 위해 정규 표현식 (regex) 을 사용하여 단어 경계를 식별합니다. Python 의 `re` 모듈은 이 작업에 사용할 수 있는 강력한 패턴 매칭 기능을 제공합니다.

camelCase 문자열을 처리하도록 함수를 업데이트해 보겠습니다:

1.  먼저 소문자 뒤에 대문자가 오는 패턴 (예: "camelCase") 을 식별해야 합니다.
2.  그런 다음 그 사이에 공백을 삽입합니다.
3.  마지막으로 모든 문자를 소문자로 변환하고 공백을 밑줄로 바꿉니다.

`snake_case.py` 파일을 이 개선된 함수로 업데이트하십시오:

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

이 함수가 수행하는 작업을 자세히 살펴보겠습니다:

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)`는 소문자 `([a-z])` 뒤에 대문자 `([A-Z])`가 오는 패턴을 찾습니다. 그런 다음 이 패턴을 동일한 문자로 바꾸지만 캡처된 그룹을 참조하는 `\1` 및 `\2`를 사용하여 그 사이에 공백을 추가합니다.
- 그런 다음 `lower()`를 사용하여 모든 문자를 소문자로 변환하고 공백을 밑줄로 바꿉니다.

스크립트를 다시 실행하여 camelCase 에 대해 작동하는지 확인하십시오:

```bash
python3 ~/project/snake_case.py
```

이제 출력은 다음과 같아야 합니다:

```
Original: helloWorld
Snake case: hello_world
```

훌륭합니다! 이제 함수가 camelCase 문자열을 처리할 수 있습니다. 다음 단계에서는 더 복잡한 경우를 처리하도록 개선할 것입니다.
