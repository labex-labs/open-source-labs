# Pascal Case 함수 향상 및 사용

이제 작동하는 `toPascalCase` 함수가 있으므로 추가 기능으로 향상시키고 실용적인 방식으로 사용하는 방법을 알아보겠습니다.

1. WebIDE 에서 `pascalCase.js` 파일을 엽니다.

2. 가장자리 사례를 더 잘 처리하도록 함수를 수정해 보겠습니다. 기존 코드를 다음으로 바꿉니다.

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Handle edge cases
  if (!str) return "";
  if (typeof str !== "string") return "";

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

// Test cases including edge cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("")); // ""
console.log(toPascalCase(null)); // ""
console.log(toPascalCase("123_abc")); // "123Abc"
console.log(toPascalCase("UPPER_CASE_EXAMPLE")); // "UpperCaseExample"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"

// Create a reusable utility module
module.exports = { toPascalCase };
```

3. Ctrl+S 를 눌러 파일을 저장합니다.

4. 이제 다른 파일에서 함수를 유틸리티로 사용하는 방법을 보여주기 위해 새 파일을 만들어 보겠습니다. 상단 메뉴에서 "File" > "New File"을 클릭하여 새 파일을 만듭니다.

5. 이 파일을 `/home/labex/project` 디렉토리에 `useCase.js`로 저장합니다.

6. `useCase.js`에 다음 코드를 추가합니다.

```javascript
// Import the toPascalCase function from our utility file
const { toPascalCase } = require("./pascalCase");

// Example: Converting database field names to JavaScript variable names
const databaseFields = [
  "user_id",
  "first_name",
  "last_name",
  "email_address",
  "date_of_birth"
];

// Convert each field name to Pascal case
const javaScriptVariables = databaseFields.map((field) => toPascalCase(field));

// Display the results
console.log("Database Fields:");
console.log(databaseFields);
console.log("\nJavaScript Variables (Pascal Case):");
console.log(javaScriptVariables);

// Example: Creating a class name from a description
const description = "user account manager";
const className = toPascalCase(description);
console.log(`\nClass name created from "${description}": ${className}`);
```

7. Ctrl+S 를 눌러 파일을 저장합니다.

8. Node.js 를 사용하여 새 파일을 실행합니다. 터미널에서 다음을 입력합니다.

```bash
node useCase.js
```

다음과 유사한 출력이 표시되어야 합니다.

```
Database Fields:
[ 'user_id', 'first_name', 'last_name', 'email_address', 'date_of_birth' ]

JavaScript Variables (Pascal Case):
[ 'UserId', 'FirstName', 'LastName', 'EmailAddress', 'DateOfBirth' ]

Class name created from "user account manager": UserAccountManager
```

이는 데이터베이스 필드 이름을 JavaScript 변수 이름으로 변환하고 설명에서 클래스 이름을 만드는 데 `toPascalCase` 함수를 실용적으로 사용하는 것을 보여줍니다.

또한 다음을 추가했습니다.

1. null, undefined 또는 문자열이 아닌 입력에 대한 오류 처리
2. 함수를 다른 파일로 가져올 수 있도록 모듈 내보내기
3. 함수의 실제 사용 예시

이러한 향상으로 `toPascalCase` 함수는 실제 JavaScript 애플리케이션에서 더욱 강력하고 유용하게 사용할 수 있습니다.
