# Capitalizando Cada Palavra

Agora que podemos dividir uma string em palavras, precisamos capitalizar a primeira letra de cada palavra e colocar o restante em minúsculas. Vamos implementar essa funcionalidade.

1. Em sua sessão do Node.js, vamos escrever uma função para capitalizar uma única palavra. Digite:

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Teste com alguns exemplos
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

A saída deve ser:

```
Hello
World
Javascript
```

2. Agora, vamos aplicar esta função a um array de palavras usando o método `map()`. Digite:

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

A saída deve ser:

```
[ 'Hello', 'World', 'Javascript' ]
```

O método `map()` cria um novo array aplicando uma função a cada elemento do array original. Neste caso, estamos aplicando nossa função `capitalizeWord` a cada palavra.

3. Finalmente, vamos juntar as palavras capitalizadas para formar uma string Pascal case:

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

A saída deve ser:

```
HelloWorldJavascript
```

O método `join("")` combina todos os elementos de um array em uma única string, usando o delimitador fornecido (uma string vazia neste caso) entre cada elemento.

Esses passos demonstram o processo principal de conversão de uma string para Pascal case:

1. Dividir a string em palavras
2. Capitalizar cada palavra
3. Juntar as palavras sem nenhum separador
