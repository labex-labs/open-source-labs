# Como Truncar uma String em Espaços em Branco em JavaScript

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está uma função que trunca uma string até um comprimento especificado, respeitando os espaços em branco sempre que possível:

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

Para usar esta função, passe a string que você deseja truncar como o primeiro argumento, o comprimento máximo como o segundo argumento e uma string de finalização opcional como o terceiro argumento. Se o comprimento da string for menor ou igual ao limite especificado, a string original será retornada. Caso contrário, a função encontrará o último espaço antes do limite e truncará a string nesse ponto, adicionando a string de finalização, se especificada.

Aqui estão alguns exemplos:

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
