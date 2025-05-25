# Função para Mapear as Chaves de um Objeto

Para mapear as chaves de um objeto usando uma função fornecida e gerar um novo objeto, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.keys()` para iterar sobre as chaves do objeto.
3.  Use `Array.prototype.reduce()` para criar um novo objeto com os mesmos valores e chaves mapeadas usando a função fornecida (`fn`).

Aqui está um exemplo de implementação da função `mapKeys`:

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

Você pode testar a função com uma entrada de exemplo como esta:

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
