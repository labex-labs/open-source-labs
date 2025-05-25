# Verificar se uma String é JSON Válido

Para verificar se uma determinada string é JSON válido, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `JSON.parse()` e um bloco `try...catch` para verificar se a string fornecida é JSON válido.
3.  Se a string for válida, retorne `true`. Caso contrário, retorne `false`.

Aqui está um trecho de código de exemplo que implementa essa lógica:

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

Você pode testar esta função com diferentes strings de entrada, assim:

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

No último exemplo, `null` não é uma string JSON válida, então a função retorna `false`.
