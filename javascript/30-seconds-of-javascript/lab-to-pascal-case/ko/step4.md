# 완전한 toPascalCase 함수 생성

이제 필요한 모든 구성 요소를 이해했으므로 모든 입력 문자열을 처리할 수 있는 완전한 `toPascalCase` 함수를 만들어 보겠습니다.

1. 함수를 저장할 JavaScript 파일을 만들어 보겠습니다. Ctrl+C 를 두 번 누르거나 `.exit`를 입력하여 Node.js 세션을 종료합니다.

2. WebIDE 에서 상단 메뉴에서 "File" > "New File"을 클릭하여 새 파일을 만듭니다.

3. 파일을 `/home/labex/project` 디렉토리에 `pascalCase.js`로 저장합니다.

4. 다음 코드를 복사하여 편집기에 붙여넣습니다.

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Ctrl+S 를 누르거나 메뉴에서 "File" > "Save"를 선택하여 파일을 저장합니다.

6. 터미널을 열고 다음을 입력하여 Node.js 를 사용하여 파일을 실행합니다.

```bash
node pascalCase.js
```

다음 출력이 표시되어야 합니다.

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

이제 `toPascalCase` 함수가 올바르게 작동합니다. 작동 방식을 검토해 보겠습니다.

1. 사용된 구분 기호에 관계없이 정규 표현식을 사용하여 입력 문자열의 단어를 일치시킵니다.
2. 단어가 발견되었는지 확인합니다. 그렇지 않은 경우 빈 문자열을 반환합니다.
3. `map()`을 사용하여 각 단어를 대문자화하고 `join('')`을 사용하여 구분 기호 없이 결합합니다.
4. 결과는 각 단어가 대문자로 시작하고 나머지는 소문자인 Pascal case 문자열입니다.
