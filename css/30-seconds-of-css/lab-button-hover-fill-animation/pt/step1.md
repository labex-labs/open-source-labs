# Animação de Preenchimento (Fill Animation) em Botão

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de preenchimento (fill animation) ao passar o mouse (hover), você pode definir as propriedades `color` e `background` e aplicar uma `transition` apropriada para animar as mudanças. Para acionar a animação ao passar o mouse, use a pseudo-classe `:hover` para alterar as propriedades `background` e `color` do elemento. Aqui está um exemplo de trecho de código:

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
