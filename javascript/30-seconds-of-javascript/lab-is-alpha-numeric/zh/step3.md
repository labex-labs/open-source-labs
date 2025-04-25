# 创建一个简单的验证工具

既然我们已经理解了字母数字检查函数，接下来让我们构建一个简单的交互式验证工具。我们将使用 Node.js 的内置 `readline` 模块从终端获取用户输入。

在同一目录下创建一个名为 `validator.js` 的新文件：

1. 在文件资源管理器面板中右键单击
2. 选择“New File”
3. 将文件命名为 `validator.js`

在文件中添加以下代码：

```javascript
const readline = require("readline");

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Function to check the input
function checkInput(input) {
  if (isAlphaNumeric(input)) {
    console.log(`"${input}" is alphanumeric.`);
  } else {
    console.log(`"${input}" is NOT alphanumeric.`);
    console.log(
      "Alphanumeric strings contain only letters (A-Z, a-z) and numbers (0-9)."
    );
  }

  // Ask if the user wants to check another string
  rl.question("\nDo you want to check another string? (yes/no): ", (answer) => {
    if (answer.toLowerCase() === "yes" || answer.toLowerCase() === "y") {
      askForInput();
    } else {
      console.log("Thank you for using the alphanumeric validator!");
      rl.close();
    }
  });
}

// Function to ask for input
function askForInput() {
  rl.question("Enter a string to check if it is alphanumeric: ", (input) => {
    checkInput(input);
  });
}

// Welcome message
console.log("=== Alphanumeric String Validator ===");
console.log(
  "This tool checks if a string contains only alphanumeric characters (A-Z, a-z, 0-9).\n"
);

// Start the program
askForInput();
```

保存文件并使用以下命令运行：

```bash
node validator.js
```

你将看到一条欢迎消息和一个提示，要求你输入一个字符串。尝试输入不同的字符串，例如：

- `hello123`（字母数字字符串）
- `Hello World`（由于包含空格，不是字母数字字符串）
- `hello@123`（由于包含 @ 符号，不是字母数字字符串）

对于每个输入，程序会告诉你它是否为字母数字字符串，并询问你是否要检查另一个字符串。输入 `yes` 或 `y` 继续，输入其他内容则退出程序。

这个交互式工具展示了如何在实际应用中使用我们的字母数字验证函数。
