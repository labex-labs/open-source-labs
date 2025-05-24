# Instruções para Converter Map em Objeto em JavaScript

Para converter um `Map` JavaScript em um objeto, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Map.prototype.entries()` para converter o `Map` em um array de pares chave-valor.
3.  Use o método `Object.fromEntries()` para converter o array em um objeto.

Aqui está um trecho de código de exemplo para converter um `Map` em um objeto:

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

Para testar a função, você pode executar:

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
