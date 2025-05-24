# Como Obter o Nome de uma Função em JavaScript

Para obter o nome de uma função JavaScript, siga estes passos:

1.  Abra o Terminal ou SSH.
2.  Digite `node` para começar a praticar a codificação.
3.  Use `console.debug()` e a propriedade `name` da função passada para registrar o nome da função no canal `debug` do console.
4.  Retorne a função `fn` fornecida.

Aqui está um trecho de código de exemplo que demonstra como obter o nome de uma função em JavaScript:

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// The function name 'max' is logged in the debug channel of the console.
// m = 6
```

Neste exemplo, a função `functionName` registra o nome da função passada no canal `debug` do console e retorna a própria função. A propriedade `name` da função é usada para obter seu nome.
