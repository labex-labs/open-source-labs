# Como Escapar Expressões Regulares em JavaScript

Para escapar uma string para usá-la em uma expressão regular em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.replace()` para escapar caracteres especiais.
3.  Copie e cole o seguinte trecho de código:

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4.  Use a função `escapeRegExp()` para escapar caracteres especiais em uma string.

Aqui está um exemplo:

```js
escapeRegExp("(test)"); // \\(test\\)
```

Com estes passos, você pode agora facilmente escapar qualquer caractere especial em uma expressão regular em JavaScript.
