# 실용적인 예제 파일 만들기

이제 바이트 크기 함수를 보다 실용적인 방식으로 구현하기 위해 JavaScript 파일을 만들어 보겠습니다. 이는 이 함수를 실제 응용 프로그램에서 사용하는 방법을 보여줍니다.

1. WebIDE 에서 새 파일을 만듭니다. 파일 탐색기 사이드바에서 "New File" 아이콘을 클릭하고 이름을 `byteSizeCalculator.js`로 지정합니다.

2. 다음 코드를 파일에 추가합니다.

```javascript
/**
 * 주어진 문자열의 바이트 크기를 계산합니다.
 * @param {string} str - 바이트 크기를 계산할 문자열입니다.
 * @returns {number} 바이트 단위의 크기입니다.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// 다양한 유형의 문자열 예시
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界！",
  "😀😃😄😁"
];

// 결과 표시
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Ctrl+S 를 누르거나 메뉴에서 File > Save 를 선택하여 파일을 저장합니다.

4. 터미널에서 파일을 실행합니다.

```bash
node byteSizeCalculator.js
```

다음과 유사한 출력을 볼 수 있습니다.

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

이 표는 다양한 유형의 문자열에 대한 문자 수와 바이트 크기의 차이를 명확하게 보여줍니다.

이러한 차이점을 이해하는 것은 다음과 같은 경우에 중요합니다.

- 웹 양식에서 사용자 입력에 대한 제한 설정
- 텍스트 데이터의 저장 요구 사항 계산
- 크기 제한이 있는 API 작업
- 네트워크를 통한 데이터 전송 최적화
