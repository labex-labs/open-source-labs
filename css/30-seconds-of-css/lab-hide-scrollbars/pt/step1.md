# Ocultar Barras de Rolagem

`index.html` e `style.css` já foram fornecidos na VM.

Para permitir que um elemento seja rolável enquanto oculta as barras de rolagem, siga estes passos:

- Use `overflow: auto` para habilitar a rolagem no elemento.
- Use `scrollbar-width: none` para ocultar as barras de rolagem no Firefox.
- Use `display: none` no pseudo-elemento `::-webkit-scrollbar` para ocultar as barras de rolagem em navegadores WebKit (como Chrome, Edge e Safari).

Aqui está um exemplo de implementação:

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
