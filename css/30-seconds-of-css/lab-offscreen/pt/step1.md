# Offscreen (Fora da Tela)

`index.html` e `style.css` já foram fornecidos na VM.

Esta técnica oculta completamente um elemento no DOM, ao mesmo tempo em que o torna acessível. Para conseguir isso, você pode seguir estas etapas:

- Remova todas as bordas e preenchimentos (padding) e oculte o overflow do elemento.
- Use `clip` para garantir que nenhuma parte do elemento seja exibida.
- Defina a `height` (altura) e a `width` (largura) do elemento para `1px` e negue-as usando `margin: -1px`.
- Use `position: absolute` para evitar que o elemento ocupe espaço no DOM.
- Observe que esta técnica é uma alternativa melhor a `display: none` (não legível por leitores de tela) e `visibility: hidden` (ocupa espaço físico no DOM) em termos de acessibilidade e amigabilidade ao layout.

Aqui está um exemplo de como você pode usar essa técnica em HTML e CSS:

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
