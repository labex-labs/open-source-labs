# Estilizar Links Sem Texto

`index.html` e `style.css` já foram fornecidos na VM.

Para exibir a URL do link para links que não possuem texto, você pode usar a pseudo-classe `:empty` para selecionar esses links, a pseudo-classe `:not` para excluir links com texto e a propriedade `content` em combinação com a função `attr()` para exibir a URL do link no pseudo-elemento `::before`. Aqui está um exemplo de trecho de código:

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
