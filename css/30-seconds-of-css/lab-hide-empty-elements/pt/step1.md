# Ocultar Elementos Vazios

`index.html` e `style.css` já foram fornecidos na VM (Virtual Machine).

Para ocultar elementos sem conteúdo, use a pseudo-classe `:empty`. Por exemplo, se você tiver o seguinte código HTML:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

Você pode usar o seguinte código CSS para ocultar o elemento button sem conteúdo:

```css
p:empty {
  display: none;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
