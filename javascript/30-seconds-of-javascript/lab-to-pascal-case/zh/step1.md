# 理解帕斯卡命名法（Pascal Case）并搭建环境

帕斯卡命名法是一种命名约定，其规则如下：

- 每个单词的首字母大写
- 单词之间不使用空格、连字符或下划线
- 其他所有字母均为小写

例如：

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

让我们从搭建开发环境开始。

1. 通过点击顶部菜单栏中的 “Terminal”，从 WebIDE 界面打开终端。

2. 在终端中输入以下命令并按回车键，启动 Node.js 交互式会话：

```bash
node
```

你应该会看到 Node.js 提示符 (`>`) 出现，这表明你现在已进入 Node.js 交互式环境。

3. 让我们尝试一个简单的字符串操作来热热身。在 Node.js 提示符处输入以下代码：

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

输出应该是：

```
John doe
```

这个简单的示例展示了如何将字符串的首字母大写。我们使用了：

- `charAt(0)` 来获取第一个字符
- `toUpperCase()` 将其转换为大写
- `slice(1)` 来获取字符串的其余部分
- 使用 `+` 进行拼接以组合它们

在构建帕斯卡命名法转换器时，这些字符串方法会很有用。
