# Mapeamento Profundo de Chaves de Objeto

Para mapear profundamente as chaves de um objeto, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `deepMapKeys` com o objeto fornecido e uma função que gera novas chaves.
3.  A função cria um objeto com os mesmos valores do objeto fornecido e chaves geradas executando a função fornecida para cada chave.
4.  Itere sobre as chaves do objeto usando `Object.keys()`.
5.  Crie um novo objeto com os mesmos valores e chaves mapeadas usando `Array.prototype.reduce()` e a função fornecida.
6.  Se um valor for um objeto, chame recursivamente `deepMapKeys` nele para mapear suas chaves também.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

Aqui está um exemplo de uso de `deepMapKeys`:

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
