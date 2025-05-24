# Como Capitalizar Cada Palavra em JavaScript

Para capitalizar cada palavra em uma string usando JavaScript, você pode usar o método `String.prototype.replace()` para corresponder ao primeiro caractere de cada palavra e, em seguida, usar o método `String.prototype.toUpperCase()` para capitalizá-lo.

Aqui está um trecho de código de exemplo que você pode usar:

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

Para usar esta função, passe a string que você deseja capitalizar como um argumento, assim:

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

Isso retornará a string capitalizada 'Hello World!'.
