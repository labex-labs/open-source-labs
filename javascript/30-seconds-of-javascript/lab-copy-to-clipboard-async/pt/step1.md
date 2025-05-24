# Função para Copiar uma String para a Área de Transferência

Para copiar uma string para a área de transferência, use a função `copyToClipboardAsync`. A função retorna uma promise que é resolvida quando o conteúdo da área de transferência foi atualizado. Aqui estão os passos:

1.  Verifique se a API Clipboard está disponível, verificando se `Navigator`, `Navigator.clipboard` e `Navigator.clipboard.writeText` são truthy usando uma declaração `if`.
2.  Se a API Clipboard estiver disponível, use `Clipboard.writeText()` para escrever o valor fornecido, `str`, na área de transferência.
3.  Retorne o resultado de `Clipboard.writeText()`, que é uma promise que é resolvida quando o conteúdo da área de transferência foi atualizado.
4.  Se a API Clipboard não estiver disponível, rejeite a promise com uma mensagem de erro apropriada usando `Promise.reject()`.
5.  Se precisar suportar navegadores mais antigos, use `Document.execCommand()` em vez de `Clipboard.writeText()`. Você pode descobrir mais sobre isso no snippet `copyToClipboard`.

Aqui está a função `copyToClipboardAsync`:

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

Para usar a função, chame `copyToClipboardAsync` com a string que você deseja copiar como um argumento, assim:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' copied to clipboard.
```
