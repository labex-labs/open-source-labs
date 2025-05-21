# 함수 최적화 및 엣지 케이스 (Edge Case) 테스트

저희 함수는 기본적인 경우에 작동하지만, 최적화하고 몇 가지 엣지 케이스를 처리해 보겠습니다:

1. 입력 문자열이 비어 있는지 확인해야 합니다.
2. 정규 표현식 (regex) 처리를 단순화할 수 있습니다.
3. 대체 문자열이 문자열이 아닌 경우를 처리해야 합니다.

다음과 같은 최적화로 `replaceLast` 함수를 업데이트하십시오:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure str is a string
  if (typeof str !== "string") {
    return str;
  }

  // If str is empty or pattern is not provided, return original string
  if (str === "" || pattern === undefined) {
    return str;
  }

  // Ensure replacement is a string
  if (replacement === undefined) {
    replacement = "";
  } else if (typeof replacement !== "string") {
    replacement = String(replacement);
  }

  // Handle string patterns
  if (typeof pattern === "string") {
    const lastIndex = str.lastIndexOf(pattern);
    if (lastIndex === -1) {
      return str;
    }
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + pattern.length)
    );
  }

  // Handle regular expression patterns
  if (pattern instanceof RegExp) {
    // Create a global version of the regex to find all matches
    const globalRegex = new RegExp(
      pattern.source,
      "g" + (pattern.ignoreCase ? "i" : "") + (pattern.multiline ? "m" : "")
    );

    // Find all matches
    const matches = str.match(globalRegex);

    // If no matches, return original string
    if (!matches || matches.length === 0) {
      return str;
    }

    // Get the last match
    const lastMatch = matches[matches.length - 1];

    // Find the position of the last match
    const lastIndex = str.lastIndexOf(lastMatch);

    // Rebuild the string with the replacement
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + lastMatch.length)
    );
  }

  // If pattern is neither string nor RegExp, return original string
  return str;
}
```

엣지 케이스를 다루기 위해 더 많은 테스트 케이스를 추가해 봅시다:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)

// Test cases for regular expression patterns
console.log(replaceLast("Hello world world", /world/, "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("123 456 789", /\d+/, "numbers")); // Should output: "123 456 numbers"
console.log(replaceLast("abcdef", /xyz/, "123")); // Should output: "abcdef" (pattern not found)

// Edge cases
console.log(replaceLast("", "abc", "123")); // Should output: "" (empty string)
console.log(replaceLast("abcdef", "", "123")); // Should output: "abcde123f" (empty pattern)
console.log(replaceLast("abcdef", "def", "")); // Should output: "abc" (empty replacement)
console.log(replaceLast("AbCdEf", /[a-z]/, "X")); // Should output: "AbCdEX" (case-sensitive regex)
console.log(replaceLast("AbCdEf", /[a-z]/i, "X")); // Should output: "AbCdEX" (case-insensitive regex)
```

업데이트된 출력을 확인하기 위해 코드를 다시 실행하십시오:

```bash
node replaceLast.js
```

이 버전의 함수는 더 많은 엣지 케이스를 처리하고 깔끔한 코드를 유지합니다. 이제 프로젝트에서 사용할 준비가 된 강력한 `replaceLast` 함수가 있습니다.
