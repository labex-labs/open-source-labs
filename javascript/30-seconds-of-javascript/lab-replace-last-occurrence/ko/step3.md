# 정규 표현식 (Regular Expression) 패턴 처리

이제 정규 표현식 패턴을 처리하도록 함수를 개선해 봅시다. 패턴이 정규 표현식인 경우 다음을 수행해야 합니다:

1. 문자열에서 모든 일치 항목을 찾습니다.
2. 마지막 일치 항목을 가져옵니다.
3. 마지막 일치 항목을 대체 문자열로 바꿉니다.

정규 표현식 패턴을 처리하도록 `replaceLast` 함수를 업데이트하십시오:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  // Handle string patterns
  if (typeof pattern === "string") {
    const lastIndex = str.lastIndexOf(pattern);
    if (lastIndex === -1) {
      return str;
    }
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // Handle regular expression patterns
  if (pattern instanceof RegExp) {
    // Create a new RegExp with global flag to find all matches
    const globalRegex = new RegExp(pattern.source, "g");

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
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + lastMatch.length);
    return before + replacement + after;
  }

  // If pattern is neither string nor RegExp, return original string
  return str;
}
```

정규 표현식 패턴에 대한 테스트 케이스를 추가하십시오:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)

// Test cases for regular expression patterns
console.log(replaceLast("Hello world world", /world/, "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("123 456 789", /\d+/, "numbers")); // Should output: "123 456 numbers"
console.log(replaceLast("abcdef", /xyz/, "123")); // Should output: "abcdef" (pattern not found)
```

업데이트된 출력을 확인하기 위해 코드를 다시 실행하십시오:

```bash
node replaceLast.js
```

이제 문자열 패턴과 정규 표현식 패턴 모두 `replaceLast` 함수에서 올바르게 작동해야 합니다.
