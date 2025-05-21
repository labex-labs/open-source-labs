# 영숫자 문자 이해

영숫자 문자는 영어 알파벳의 26 개 문자 (대문자 A-Z 및 소문자 a-z 모두) 와 10 개의 숫자 (0-9) 로 구성됩니다. 문자열이 영숫자인지 확인할 때, 우리는 해당 문자열이 이러한 문자만 포함하고 다른 것은 포함하지 않는지 확인하는 것입니다.

JavaScript 에서는 정규 표현식 (regular expression) 을 사용하여 영숫자 문자를 확인할 수 있습니다. 정규 표현식 (regex) 은 문자열에서 문자 조합을 일치시키는 데 사용되는 패턴입니다.

코드 편집기를 열어 시작해 보겠습니다. WebIDE 에서 왼쪽의 파일 탐색기로 이동하여 새 JavaScript 파일을 만듭니다.

1. 파일 탐색기 패널에서 마우스 오른쪽 버튼을 클릭합니다.
2. "New File"을 선택합니다.
3. 파일 이름을 `alphanumeric.js`로 지정합니다.

파일을 만들면 편집기에서 자동으로 열립니다. 그렇지 않은 경우 파일 탐색기에서 `alphanumeric.js`를 클릭하여 엽니다.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

이제 다음 코드를 입력해 보겠습니다.

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

`Ctrl+S`를 누르거나 메뉴에서 "File" > "Save"를 선택하여 파일을 저장합니다.

이제 이 JavaScript 파일을 실행하여 출력을 확인해 보겠습니다. 메뉴에서 "Terminal" > "New Terminal"을 선택하거나 `` Ctrl+` ``를 눌러 WebIDE 에서 터미널을 엽니다.

터미널에서 다음 명령을 실행합니다.

```bash
node alphanumeric.js
```

다음 출력을 볼 수 있습니다.

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

이 출력은 함수가 `hello123`과 `123`을 영숫자 문자열로 올바르게 식별하는 반면, `hello 123`(공백 포함) 과 `hello@123`(특수 문자 @ 포함) 은 영숫자가 아님을 보여줍니다.
