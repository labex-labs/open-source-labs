# React useCopyToClipboard Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para copiar o texto fornecido para a área de transferência (clipboard), use o snippet `copyToClipboard` fornecido em `/js/s/copy-to-clipboard/` junto com o hook `useState()` para inicializar a variável `copied`. Para criar um callback para o método `copyToClipboard`, use o hook `useCallback()`. Para redefinir a variável de estado `copied` quando o `text` muda, use o hook `useEffect()`. Finalmente, retorne a variável de estado `copied` e o callback `copy`.

O código a seguir demonstra um exemplo de como usar esses hooks e métodos para criar um componente `TextCopy`. Quando o usuário clica no botão "Click to copy", a função `copy` é chamada e a variável `copied` é definida como `true`. Se a cópia for bem-sucedida, "Copied!" será exibido.

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
