# Compreendendo Caracteres Alfanuméricos

Caracteres alfanuméricos consistem nas 26 letras do alfabeto inglês (tanto maiúsculas A-Z quanto minúsculas a-z) e nos 10 dígitos numéricos (0-9). Quando verificamos se uma string é alfanumérica, estamos verificando se ela contém apenas esses caracteres e nada mais.

Em JavaScript, podemos verificar caracteres alfanuméricos usando expressões regulares (regular expressions). Expressões regulares (regex) são padrões usados para corresponder combinações de caracteres em strings.

Vamos começar abrindo nosso editor de código. No WebIDE, navegue até o explorador de arquivos no lado esquerdo e crie um novo arquivo JavaScript:

1.  Clique com o botão direito no painel do explorador de arquivos
2.  Selecione "Novo Arquivo"
3.  Nomeie o arquivo `alphanumeric.js`

Depois de criar o arquivo, ele deve abrir automaticamente no editor. Caso contrário, clique em `alphanumeric.js` no explorador de arquivos para abri-lo.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

Agora, vamos inserir o seguinte código:

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

Salve o arquivo pressionando `Ctrl+S` ou selecionando "Arquivo" > "Salvar" no menu.

Agora, vamos executar este arquivo JavaScript para ver a saída. Abra o terminal no WebIDE selecionando "Terminal" > "Novo Terminal" no menu ou pressionando `` Ctrl+` ``.

No terminal, execute o seguinte comando:

```bash
node alphanumeric.js
```

Você deve ver a seguinte saída:

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

Esta saída mostra que nossa função identifica corretamente `hello123` e `123` como strings alfanuméricas, enquanto `hello 123` (contém um espaço) e `hello@123` (contém um caractere especial @) não são alfanuméricos.
