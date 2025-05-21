# 문제 이해

snake case 변환 함수를 작성하기 전에, 우리가 무엇을 달성해야 하는지 이해해 봅시다:

1.  어떤 형식의 문자열이든 snake case 로 변환해야 합니다.
2.  Snake case 는 단어 사이에 밑줄이 있는 소문자를 의미합니다.
3.  다양한 입력 형식을 처리해야 합니다:
    - camelCase (예: `camelCase` → `camel_case`)
    - 공백이 있는 문자열 (예: `some text` → `some_text`)
    - 혼합된 형식의 문자열 (예: 하이픈, 밑줄 및 대소문자 혼합)

snake case 함수를 위해 새로운 Python 파일을 만들어 보겠습니다. WebIDE 에서 프로젝트 디렉토리로 이동하여 `snake_case.py`라는 새 파일을 만듭니다:

```python
# This function will convert a string to snake case
def snake(s):
    # We'll implement this function step by step
    pass  # Placeholder for now

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

이 파일을 저장합니다. 다음 단계에서는 함수를 구현하기 시작합니다.

지금은 파일이 올바르게 설정되었는지 확인하기 위해 자리 표시자 함수를 실행해 보겠습니다. 터미널을 열고 다음을 실행합니다:

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

다음과 같은 출력이 표시되어야 합니다:

```
Original: helloWorld
Snake case: None
```

결과가 `None`인 이유는 현재 함수가 기본 Python `None` 값을 반환하기 때문입니다. 다음 단계에서는 실제 변환 로직을 추가합니다.
