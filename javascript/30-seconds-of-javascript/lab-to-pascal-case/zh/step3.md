# 大写每个单词

既然我们已经能够将字符串拆分为单词，接下来就需要将每个单词的首字母大写，并将其余字母小写。下面来实现这个功能。

1. 在你的 Node.js 会话中，编写一个函数来大写单个单词。输入：

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

输出应该是：

```
Hello
World
Javascript
```

2. 现在，使用 `map()` 方法将这个函数应用到单词数组上。输入：

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

输出应该是：

```
[ 'Hello', 'World', 'Javascript' ]
```

`map()` 方法通过对原数组的每个元素应用一个函数来创建一个新数组。在这种情况下，我们将 `capitalizeWord` 函数应用到每个单词上。

3. 最后，将大写后的单词连接起来，形成一个帕斯卡命名法（Pascal case）的字符串：

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

输出应该是：

```
HelloWorldJavascript
```

`join("")` 方法将数组的所有元素组合成一个字符串，在每个元素之间使用指定的分隔符（这里是一个空字符串）。

这些步骤展示了将字符串转换为帕斯卡命名法的核心过程：

1. 将字符串拆分为单词
2. 大写每个单词
3. 无分隔符地连接这些单词
