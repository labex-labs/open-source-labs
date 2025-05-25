# Gerando um Código de Cor Hexadecimal Aleatório no Terminal/SSH

Para gerar um código de cor hexadecimal aleatório no Terminal/SSH, siga os passos abaixo:

1.  Abra o Terminal/SSH.
2.  Digite `node`.
3.  Use o seguinte código para gerar um número hexadecimal de 24 bits (6 \* 4 bits) aleatório:

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4.  Para gerar um código de cor hexadecimal aleatório, chame a função `randomHexColorCode()`.

Exemplo:

```js
randomHexColorCode(); // '#e34155'
```

Isso gerará um código de cor hexadecimal aleatório que você pode usar em seus projetos de codificação.
