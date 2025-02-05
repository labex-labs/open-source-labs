# 变量

> 打开终端/SSH 并输入 `node` 开始练习编码。

变量是存储值的容器。你可以使用 `let` 关键字声明一个变量，后跟你给变量起的名字：

```js
let myVariable;
```

行尾的分号表示语句的结束位置。只有在需要在同一行分隔语句时才需要使用。不过，有些人认为在每个语句末尾都加分号是个好习惯。关于何时应该使用和不应该使用分号还有其他规则。

你几乎可以给变量起任何名字，但有一些限制。如果你不确定，可以[检查你的变量名](https://mothereff.in/js-variables)，看看它是否有效。

JavaScript 区分大小写。这意味着 `myVariable` 与 `myvariable` 不一样。如果你的代码有问题，检查一下大小写！

声明变量后，你可以给它赋值：

```js
myVariable = "Bob";
```

此外，你可以在同一行上进行这两个操作：

```js
let myVariable = "Bob";
```

你可以通过调用变量名来获取值：

```js
myVariable;
```

给变量赋值后，你可以在代码后面更改它：

```js
let myVariable = "Bob";
myVariable = "Steve";
```

请注意，变量可以保存具有不同[数据类型](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)的值：

| 变量                                                                | 解释                                                                                      | 示例                                                                                                     |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [字符串](https://developer.mozilla.org/en-US/docs/Glossary/String)  | 这是一串文本，称为字符串。为了表明该值是一个字符串，用单引号或双引号将其括起来。          | `let myVariable = 'Bob';` 或 `let myVariable = "Bob";`                                                   |
| [数字](https://developer.mozilla.org/en-US/docs/Glossary/Number)    | 这是一个数字。数字周围没有引号。                                                          | `let myVariable = 10;`                                                                                   |
| [布尔值](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | 这是一个真/假值。`true` 和 `false` 这两个词是特殊关键字，不需要引号。                     | `let myVariable = true;`                                                                                 |
| [数组](https://developer.mozilla.org/en-US/docs/Glossary/Array)     | 这是一种结构，允许你在一个引用中存储多个值。                                              | `let myVariable = [1,'Bob','Steve',10];` 像这样引用数组的每个成员：`myVariable[0]`, `myVariable[1]` 等。 |
| [对象](https://developer.mozilla.org/en-US/docs/Glossary/Object)    | 这可以是任何东西。JavaScript 中的一切都是对象，可以存储在变量中。在你学习时请记住这一点。 | `let myVariable = document.querySelector('h1');` 上述所有示例也是如此。                                  |

那么我们为什么需要变量呢？在编程中，要做任何有趣的事情都需要变量。如果值不能改变，那么你就无法做任何动态的事情，比如个性化问候消息或更改图片库中显示的图片。
