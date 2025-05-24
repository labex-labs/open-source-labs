# Desabilitar Seleção

`index.html` e `style.css` já foram fornecidos na VM.

Para tornar o conteúdo de um elemento não selecionável, adicione a propriedade CSS `user-select: none` ao seletor. No entanto, este método não é totalmente seguro para impedir que os usuários copiem conteúdo.

Exemplo:

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
