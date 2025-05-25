# Função Memoize

Para começar a codificar, abra o Terminal/SSH e digite `node`. Esta função retorna a função memoizada (em cache). Aqui estão os passos para usar esta função:

1. Instancie um novo objeto `Map` para criar um cache vazio.
2. Retorne uma função que recebe um único argumento que será fornecido à função memoizada. Antes de executar a função, verifique se a saída para esse valor de entrada específico já está em cache. Se estiver, retorne a saída em cache; caso contrário, armazene-a e retorne-a.
3. Use a palavra-chave `function` para permitir que o contexto `this` da função memoizada seja alterado, se necessário.
4. Defina o `cache` como uma propriedade na função retornada para permitir o acesso a ele.

Aqui está o código que implementa a função memoize:

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

Para ver como esta função funciona, você pode usá-la com a função `anagrams`. Aqui está um exemplo:

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // takes a long time
anagramsCached("javascript"); // returns virtually instantly since it's cached
console.log(anagramsCached.cache); // The cached anagrams map
```
