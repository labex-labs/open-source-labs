# 영숫자 문자열을 확인하는 다른 방법 탐색

정규 표현식을 사용하는 것 외에도 문자열이 영숫자인지 확인하는 다른 방법이 있습니다. `alternative-methods.js`라는 새 파일을 만들어 몇 가지 방법을 살펴보겠습니다.

1. 파일 탐색기 패널에서 마우스 오른쪽 버튼을 클릭합니다.
2. "New File"을 선택합니다.
3. 파일 이름을 `alternative-methods.js`로 지정합니다.

다음 코드를 파일에 추가합니다.

```javascript
// Method 1: Using regular expression (our original method)
function isAlphaNumericRegex(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Method 2: Using Array.every() and checking each character
function isAlphaNumericEvery(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  return [...str].every((char) => {
    const code = char.charCodeAt(0);
    // Check if character is a digit (0-9)
    const isDigit = code >= 48 && code <= 57;
    // Check if character is a lowercase letter (a-z)
    const isLowercase = code >= 97 && code <= 122;
    // Check if character is an uppercase letter (A-Z)
    const isUppercase = code >= 65 && code <= 90;

    return isDigit || isLowercase || isUppercase;
  });
}

// Method 3: Using a combination of match() and length
function isAlphaNumericMatch(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  // Remove all alphanumeric characters and check if anything remains
  const nonAlphaNumeric = str.match(/[^a-zA-Z0-9]/g);
  return nonAlphaNumeric === null;
}

// Test strings
const testStrings = [
  "hello123",
  "HELLO123",
  "hello 123",
  "hello@123",
  "",
  "0123456789",
  "abcdefghijklmnopqrstuvwxyz"
];

// Test each method with each string
console.log("=== Testing Different Methods ===");
console.log("String\t\t\tRegex\tEvery\tMatch");
console.log("---------------------------------------------");

testStrings.forEach((str) => {
  const displayStr = str.length > 10 ? str.substring(0, 10) + "..." : str;
  const paddedStr = displayStr.padEnd(16, " ");

  const regexResult = isAlphaNumericRegex(str);
  const everyResult = isAlphaNumericEvery(str);
  const matchResult = isAlphaNumericMatch(str);

  console.log(`"${paddedStr}"\t${regexResult}\t${everyResult}\t${matchResult}`);
});

console.log("\nPerformance Comparison:");
const iterations = 1000000;
const testString = "hello123ABCxyz45";

console.time("Regex Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericRegex(testString);
}
console.timeEnd("Regex Method");

console.time("Every Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericEvery(testString);
}
console.timeEnd("Every Method");

console.time("Match Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericMatch(testString);
}
console.timeEnd("Match Method");
```

파일을 저장하고 다음 명령으로 실행합니다.

```bash
node alternative-methods.js
```

출력은 각 방법이 서로 다른 테스트 문자열에서 어떻게 작동하는지 보여주고, 방법 간의 성능 비교를 보여줍니다. 정규 표현식 방법이 일반적으로 가장 간결하고 종종 가장 빠르지만, 다른 접근 방식을 이해하는 것이 유용합니다.

각 방법을 살펴보겠습니다.

1. `isAlphaNumericRegex`: 영숫자 문자만 일치시키기 위해 정규 표현식을 사용합니다.
2. `isAlphaNumericEvery`: 각 문자의 ASCII 코드를 확인하여 영숫자인지 확인합니다.
3. `isAlphaNumericMatch`: 모든 영숫자 문자를 제거하고 아무것도 남지 않는지 확인합니다.

다양한 접근 방식을 이해하면 프로그래밍 문제를 해결할 때 유연성을 얻을 수 있습니다. 정규 표현식은 강력하지만 때로는 읽기 어려울 수 있습니다. 다른 방법은 일부 프로그래머, 특히 정규식 패턴에 익숙하지 않은 프로그래머에게 더 직관적일 수 있습니다.
