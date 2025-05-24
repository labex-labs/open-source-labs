# Como Obter um Valor Aninhado em um Objeto JSON

Para recuperar um valor alvo de um objeto JSON aninhado com base em uma chave fornecida, siga estas etapas:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Verifique se o `target` existe no `obj` usando o operador `in`.
- Se o `target` for encontrado, retorne o valor correspondente no `obj`.
- Se o `target` não for encontrado, use `Object.values()` e `Array.prototype.reduce()` para chamar recursivamente a função `dig` em cada objeto aninhado até que o primeiro par chave/valor correspondente seja encontrado.

Aqui está o código para a função `dig`:

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

Para usar a função `dig`, primeiro crie um objeto JSON com níveis aninhados, assim:

```js
const data = {
  level1: {
    level2: {
      level3: "some data"
    }
  }
};
```

Em seguida, chame a função `dig` com o objeto JSON e a chave desejada:

```js
dig(data, "level3"); // 'some data'
dig(data, "level4"); // undefined
```

Esses exemplos retornarão o valor da chave `level3` no objeto `data` e `undefined` para a chave `level4` inexistente.
