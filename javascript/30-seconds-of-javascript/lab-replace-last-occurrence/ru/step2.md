# Реализация основной логики функции

Теперь, когда мы понимаем проблему, давайте реализуем основную функциональность нашей функции `replaceLast`. Сначала мы сосредоточимся на обработке строковых шаблонов, а затем в следующем шаге рассмотрим регулярные выражения.

Когда шаблон представляет собой строку, мы можем использовать метод `lastIndexOf` для нахождения позиции последнего вхождения. Как только мы знаем эту позицию, мы можем использовать метод `slice` для перестроения строки с вставленным заменяющим значением.

Обновите свою функцию `replaceLast` следующей реализацией:

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

Обновите свои тестовые случаи, чтобы проверить, правильно ли функция обрабатывает строковые шаблоны:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Запустите код еще раз, чтобы увидеть обновленный вывод:

```bash
node replaceLast.js
```

Теперь вы должны увидеть, что последнее вхождение строкового шаблона заменено в каждом тестовом случае. Например, "Hello world JavaScript" вместо "Hello world world".
