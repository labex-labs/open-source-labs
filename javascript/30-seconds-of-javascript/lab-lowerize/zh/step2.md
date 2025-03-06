# 访问对象的键

在转换对象的键之前，你需要了解如何访问它们。JavaScript 提供了 `Object.keys()` 方法，该方法会返回一个包含对象所有键的数组。

在你的 Node.js 交互式 shell 中，尝试执行以下代码：

```javascript
Object.keys(user);
```

你应该会看到如下输出：

```
[ 'Name', 'AGE', 'Email' ]
```

现在，让我们尝试使用 `toLowerCase()` 方法将每个键转换为小写。你可以使用 `map()` 方法来转换每个键：

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

输出应该是：

```
[ 'name', 'age', 'email' ]
```

很棒！现在你已经有了一个所有键都转换为小写的数组。不过，你仍然需要创建一个新对象，该对象使用这些小写键并保留原始值。为此，你将在下一步中使用 `reduce()` 方法。

在继续之前，让我们先了解一下 `reduce()` 方法。这个方法会对数组的每个元素执行一个归约函数，最终得到一个单一的输出值。

以下是一个 `reduce()` 的简单示例：

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

输出将是 `10`，这是数组中所有数字的总和。`reduce()` 方法中的 `0` 是累加器的初始值。
