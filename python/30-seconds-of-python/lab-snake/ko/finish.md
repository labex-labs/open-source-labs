# 요약

이 랩에서는 다양한 형식의 문자열을 snake case 로 변환하는 Python 함수를 만드는 방법을 배웠습니다. 다음은 여러분이 달성한 내용입니다:

1.  정규 표현식 (regular expression) 이 패턴 매칭 (pattern matching) 및 문자열 변환에 어떻게 사용될 수 있는지 배웠습니다.
2.  다음과 같은 다양한 입력 형식을 처리할 수 있는 함수를 구현했습니다:
    - camelCase (예: `camelCase` → `camel_case`)
    - PascalCase (예: `HelloWorld` → `hello_world`)
    - 공백이 있는 문자열 (예: `some text` → `some_text`)
    - 하이픈이 있는 문자열 (예: `hello-world` → `hello_world`)
    - 다양한 구분 기호와 대소문자를 사용하는 혼합 형식

사용된 주요 기술:

- `re.sub()`를 사용한 캡처 그룹 (capture group) 이 있는 정규 표현식
- `replace()`, `lower()`, `split()`, `join()`과 같은 문자열 메서드
- 다양한 명명 규칙에 대한 패턴 인식

이러한 기술은 데이터 정리, 텍스트 입력 처리 및 일관된 코딩 표준 유지에 유용합니다. 서로 다른 케이스 형식 간에 변환하는 기능은 서로 다른 명명 규칙을 사용하는 API 또는 라이브러리를 사용할 때 특히 유용합니다.
