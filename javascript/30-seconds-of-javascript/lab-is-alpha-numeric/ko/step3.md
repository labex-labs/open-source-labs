# 간단한 유효성 검사 도구 만들기

이제 영숫자 검사 함수를 이해했으므로 간단한 대화형 유효성 검사 도구를 만들어 보겠습니다. Node.js 의 내장 `readline` 모듈을 사용하여 터미널에서 사용자 입력을 받습니다.

동일한 디렉토리에 `validator.js`라는 새 파일을 만듭니다.

1. 파일 탐색기 패널에서 마우스 오른쪽 버튼을 클릭합니다.
2. "New File"을 선택합니다.
3. 파일 이름을 `validator.js`로 지정합니다.

다음 코드를 파일에 추가합니다.

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

파일을 저장하고 다음 명령으로 실행합니다.

```bash
node validator.js
```

환영 메시지와 문자열을 입력하라는 메시지가 표시됩니다. 다음과 같은 다양한 문자열을 입력해 보세요.

- `hello123` (영숫자)
- `Hello World` (공백 때문에 영숫자가 아님)
- `hello@123` (@ 기호 때문에 영숫자가 아님)

각 입력에 대해 프로그램은 영숫자인지 여부를 알려주고 다른 문자열을 확인할지 묻습니다. 계속하려면 `yes` 또는 `y`를 입력하고, 프로그램을 종료하려면 다른 응답을 입력합니다.

이 대화형 도구는 영숫자 유효성 검사 함수가 실제 응용 프로그램에서 어떻게 사용될 수 있는지 보여줍니다.
