# Ligação Automática de Texto

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este componente renderiza uma string como texto simples, com URLs convertidas em elementos de link apropriados.

Para conseguir isso, ele usa `String.prototype.split()` e `String.prototype.match()` com uma expressão regular para encontrar URLs na string fornecida. As URLs correspondentes são então retornadas como elementos `<a>`, lidando com prefixos de protocolo ausentes, se necessário. As partes restantes da string são renderizadas como texto simples.

Aqui está o código:

```jsx
const AutoLink = ({ text }) => {
  const urlRegex =
    /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  const renderText = () => {
    return text.split(urlRegex).map((word, index) => {
      const urlMatch = word.match(urlRegex);
      if (urlMatch) {
        const url = urlMatch[0];
        return (
          <a key={index} href={url.startsWith("http") ? url : `http://${url}`}>
            {url}
          </a>
        );
      }
      return <span key={index}>{word}</span>;
    });
  };

  return <div>{renderText()}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <AutoLink text="foo bar baz http://example.org bar" />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
