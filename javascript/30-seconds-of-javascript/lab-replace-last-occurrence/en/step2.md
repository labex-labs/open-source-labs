# Implementing the Core Function Logic

Now that we understand the problem, let us implement the core functionality of our `replaceLast` function. We will focus on handling string patterns first, then tackle regular expressions in the next step.

When the pattern is a string, we can use the `lastIndexOf` method to find the position of the last occurrence. Once we know this position, we can use the `slice` method to rebuild the string with the replacement inserted.

Update your `replaceLast` function with the following implementation:

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

Update your test cases to check that the function correctly handles string patterns:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Run the code again to see the updated output:

```bash
node replaceLast.js
```

You should now see the last occurrence of the string pattern replaced in each test case. For example, "Hello world JavaScript" instead of "Hello world world".
