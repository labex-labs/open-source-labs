# Como Verificar se um Valor é Null ou Undefined em JavaScript

Para determinar se um valor é `null` ou `undefined` em JavaScript, você pode usar o operador de igualdade estrita (`===`). Aqui está um exemplo de trecho de código que verifica se o valor especificado é `null` ou `undefined`:

```js
const isNil = (val) => val === undefined || val === null;
```

Você pode usar esta função para verificar se um valor é `null` ou `undefined`, assim:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

Para começar a praticar a codificação em JavaScript, você pode abrir o Terminal/SSH e digitar `node`.
