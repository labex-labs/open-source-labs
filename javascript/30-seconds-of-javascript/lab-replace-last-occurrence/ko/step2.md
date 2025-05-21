# 핵심 함수 로직 구현

이제 문제를 이해했으니, `replaceLast` 함수의 핵심 기능을 구현해 봅시다. 먼저 문자열 패턴을 처리하는 데 집중하고, 다음 단계에서 정규 표현식 (regular expression) 을 다루겠습니다.

패턴이 문자열인 경우, `lastIndexOf` 메서드를 사용하여 마지막 발생 위치를 찾을 수 있습니다. 이 위치를 알게 되면, `slice` 메서드를 사용하여 대체 문자열을 삽입하여 문자열을 다시 구성할 수 있습니다.

다음 구현으로 `replaceLast` 함수를 업데이트하십시오:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  if (typeof pattern === "string") {
    // Find the position of the last occurrence
    const lastIndex = str.lastIndexOf(pattern);

    // If pattern not found, return original string
    if (lastIndex === -1) {
      return str;
    }

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // We'll handle regex patterns in the next step
  return str;
}
```

함수가 문자열 패턴을 올바르게 처리하는지 확인하기 위해 테스트 케이스를 업데이트하십시오:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

업데이트된 출력을 확인하기 위해 코드를 다시 실행하십시오:

```bash
node replaceLast.js
```

이제 각 테스트 케이스에서 문자열 패턴의 마지막 발생이 대체된 것을 볼 수 있습니다. 예를 들어, "Hello world world" 대신 "Hello world JavaScript"가 출력됩니다.
