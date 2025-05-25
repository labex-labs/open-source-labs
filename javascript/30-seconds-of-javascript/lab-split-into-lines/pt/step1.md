# Como Começar a Praticar a Codificação no Terminal/SSH

Para começar a praticar a codificação no Terminal/SSH, simplesmente digite `node`.

# Dividindo uma String de Múltiplas Linhas em um Array de Linhas

Para dividir uma string de múltiplas linhas em um array de linhas:

- Use `String.prototype.split()` e uma expressão regular para corresponder a quebras de linha e criar um array.
- A expressão regular `/\r?\n/` corresponde tanto a quebras de linha `\r` quanto `\n`.
- Isso retornará um array de linhas.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a', 'multiline', 'string.' , '']
```
