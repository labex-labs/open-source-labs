# Função que aceita até dois argumentos

Para começar a codificar, abra o Terminal/SSH e digite `node`.

A função `binary` é criada com a capacidade de aceitar até dois argumentos, ignorando quaisquer argumentos adicionais.

A função `fn` fornecida é chamada com os dois primeiros argumentos fornecidos.

Aqui está o código:

```js
const binary = (fn) => (a, b) => fn(a, b);
```

E aqui está um exemplo de uso:

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
