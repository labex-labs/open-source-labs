# Cifra de César (Caesar Cipher)

Para usar a cifra de César, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Chame a função `caesarCipher` com a string a ser encriptada ou desencriptada, o valor de deslocamento (shift) e um booleano indicando se deve desencriptar ou não.
3.  A função `caesarCipher` usa o operador módulo (`%`) e o operador ternário (`?`) para calcular a chave de encriptação ou desencriptação correta.
4.  Ela usa o operador spread (`...`) e `Array.prototype.map()` para iterar sobre as letras da string fornecida.
5.  Ela usa `String.prototype.charCodeAt()` e `String.fromCharCode()` para converter cada letra apropriadamente, ignorando caracteres especiais, espaços, etc.
6.  Ela usa `Array.prototype.join()` para combinar todas as letras em uma string.
7.  Se você deseja desencriptar uma string encriptada, passe `true` para o último parâmetro, `decrypt`, ao chamar a função `caesarCipher`.

Aqui está o código para a função `caesarCipher`:

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

Aqui estão alguns exemplos de como usar a função `caesarCipher`:

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
