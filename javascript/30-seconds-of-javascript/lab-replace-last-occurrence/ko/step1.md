# 문제 이해 및 설정

코딩을 시작하기 전에, `replaceLast` 함수가 수행해야 할 작업을 이해해 봅시다:

1. 세 개의 매개변수를 받습니다:
   - `str`: 수정할 입력 문자열
   - `pattern`: 검색할 부분 문자열 또는 정규 표현식 (regular expression)
   - `replacement`: 마지막 발생을 대체할 문자열

2. 패턴의 마지막 발생이 대체된 새로운 문자열을 반환합니다.

함수를 구현하기 위해 JavaScript 파일을 만들어 봅시다:

1. WebIDE 파일 탐색기에서 프로젝트 디렉토리로 이동합니다.
2. `replace-last` 디렉토리에 `replaceLast.js`라는 새 파일을 만듭니다.
3. 파일에 다음 기본 구조를 추가합니다:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

모든 것이 올바르게 설정되었는지 확인하기 위해 간단한 테스트를 추가해 봅시다:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

이제 코드를 실행하여 현재 출력을 확인해 봅시다:

1. WebIDE 에서 터미널을 엽니다.
2. `replace-last` 디렉토리로 이동합니다:
   ```bash
   cd ~/project/replace-last
   ```
3. Node.js 를 사용하여 JavaScript 파일을 실행합니다:
   ```bash
   node replaceLast.js
   ```

현재 함수가 변경 사항 없이 원래 문자열을 반환하기 때문에 출력에 `Hello world world`가 표시됩니다.
