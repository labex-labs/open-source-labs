# Criando uma Ferramenta de Validação Simples

Agora que entendemos a função de verificação alfanumérica, vamos construir uma ferramenta de validação interativa simples. Usaremos o módulo `readline` embutido do Node.js para obter a entrada do usuário do terminal.

Crie um novo arquivo chamado `validator.js` no mesmo diretório:

1.  Clique com o botão direito no painel do explorador de arquivos
2.  Selecione "Novo Arquivo"
3.  Nomeie o arquivo `validator.js`

Adicione o seguinte código ao arquivo:

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

Salve o arquivo e execute-o com:

```bash
node validator.js
```

Você verá uma mensagem de boas-vindas e um prompt pedindo que você insira uma string. Tente inserir strings diferentes, como:

- `hello123` (alfanumérico)
- `Hello World` (não alfanumérico devido ao espaço)
- `hello@123` (não alfanumérico devido ao símbolo @)

Para cada entrada, o programa informará se ela é alfanumérica e perguntará se você deseja verificar outra string. Digite `yes` ou `y` para continuar, ou qualquer outra resposta para sair do programa.

Esta ferramenta interativa demonstra como nossa função de validação alfanumérica pode ser usada em uma aplicação prática.
