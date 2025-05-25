# Prática de Código: Iterando N Vezes

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Depois de fazer isso, use a seguinte função para iterar sobre um callback `n` vezes:

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

Para usar esta função, chame `times()` e passe os seguintes argumentos:

- `n`: o número de vezes que você deseja iterar sobre a função callback
- `fn`: a função callback que você deseja iterar
- `context` (opcional): o contexto que você deseja usar para a função callback (se não especificado, usará um objeto `undefined` ou o objeto global em modo não estrito)

Aqui está um exemplo de como usar a função `times()`:

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

Isso irá iterar sobre a função callback `i => (output += i)` 5 vezes e armazenar a saída na variável `output`. A saída será então registrada no console, que exibirá `01234`.
