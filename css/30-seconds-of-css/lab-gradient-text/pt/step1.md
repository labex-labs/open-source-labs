# Texto Gradiente

`index.html` e `style.css` já foram fornecidos na VM.

Para dar ao texto uma cor gradiente, você pode usar propriedades CSS. Primeiro, use a propriedade `background` com um valor `linear-gradient()` para dar ao elemento de texto um fundo gradiente. Em seguida, use `webkit-text-fill-color: transparent` para preencher o texto com uma cor transparente. Finalmente, use `webkit-background-clip: text` para recortar o fundo com o texto e preencher o texto com o fundo gradiente como a cor. Aqui está um trecho de código de exemplo:

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
