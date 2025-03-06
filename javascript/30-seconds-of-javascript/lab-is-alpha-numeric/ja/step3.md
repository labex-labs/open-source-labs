# シンプルな検証ツールの作成

英数字のチェック関数を理解したので、シンプルな対話型の検証ツールを作成しましょう。ターミナルからユーザー入力を取得するために、Node.js の組み込み `readline` モジュールを使用します。

同じディレクトリに `validator.js` という名前の新しいファイルを作成します。

1. ファイルエクスプローラーパネル内で右クリックします。
2. 「New File」を選択します。
3. ファイル名を `validator.js` とします。

ファイルに以下のコードを追加します。

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

ファイルを保存し、以下のコマンドで実行します。

```bash
node validator.js
```

歓迎メッセージと、文字列を入力するように求めるプロンプトが表示されます。次のような様々な文字列を入力してみてください。

- `hello123`（英数字）
- `Hello World`（スペースがあるため英数字ではない）
- `hello@123`（@ 記号があるため英数字ではない）

各入力に対して、プログラムはそれが英数字かどうかを教えてくれ、別の文字列をチェックするかどうかを尋ねます。続けるには `yes` または `y` を入力し、それ以外の応答を入力するとプログラムが終了します。

この対話型ツールは、英数字の検証関数が実用的なアプリケーションでどのように使用できるかを示しています。
