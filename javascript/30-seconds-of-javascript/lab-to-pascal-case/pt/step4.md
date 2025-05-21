# Criando a Função toPascalCase Completa

Agora que entendemos todos os componentes necessários, vamos criar uma função `toPascalCase` completa que pode lidar com qualquer string de entrada.

1. Vamos criar um arquivo JavaScript para salvar nossa função. Saia da sua sessão do Node.js pressionando Ctrl+C duas vezes ou digitando `.exit`.

2. No WebIDE, crie um novo arquivo clicando em "File" > "New File" no menu superior.

3. Salve o arquivo como `pascalCase.js` no diretório `/home/labex/project`.

4. Copie e cole o seguinte código no editor:

```javascript
/**
 * Converte uma string para Pascal case.
 * @param {string} str - A string de entrada para converter.
 * @returns {string} A string em Pascal case.
 */
function toPascalCase(str) {
  // Use regex para encontrar palavras, independentemente do delimitador
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // Se nenhuma palavra for encontrada, retorne uma string vazia
  if (!words) {
    return "";
  }

  // Capitalize cada palavra e junte-as
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Casos de teste
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Salve o arquivo pressionando Ctrl+S ou selecionando "File" > "Save" no menu.

6. Execute o arquivo usando Node.js abrindo o Terminal e digitando:

```bash
node pascalCase.js
```

Você deve ver a seguinte saída:

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Nossa função `toPascalCase` agora está funcionando corretamente. Vamos revisar como ela funciona:

1. Usamos uma expressão regular para encontrar palavras na string de entrada, independentemente dos delimitadores usados.
2. Verificamos se alguma palavra foi encontrada. Caso contrário, retornamos uma string vazia.
3. Usamos `map()` para capitalizar cada palavra e `join('')` para combiná-las sem separadores.
4. O resultado é uma string em Pascal case, onde cada palavra começa com uma letra maiúscula e o restante é minúsculo.
