# Função para Verificar se um Array está Contido em Outro Array

Para começar a codificar, abra o Terminal/SSH e digite `node`. Esta função verifica se todos os elementos do primeiro array estão presentes no segundo array, independentemente de sua ordem.

Aqui estão os passos a seguir:

1.  Use um loop `for...of` para iterar sobre um `Set` criado a partir do primeiro array.
2.  Aplique `Array.prototype.some()` para verificar se todos os valores distintos estão presentes no segundo array.
3.  Use `Array.prototype.filter()` para comparar o número de ocorrências de cada valor distinto em ambos os arrays.
4.  Se a contagem de qualquer elemento for maior no primeiro array do que no segundo, retorne `false`. Caso contrário, retorne `true`.

Confira o código abaixo para ver como funciona:

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

Para testar a função, use o seguinte código:

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
