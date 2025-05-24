# Animação de Borda em Botão

`index.html` e `style.css` já foram fornecidos na VM (Virtual Machine).

Para criar uma animação de borda ao passar o mouse (hover), você pode usar os pseudo-elementos `::before` e `::after` para gerar duas caixas com `24px` de largura e posicionadas acima e abaixo da caixa. Em seguida, aplique a pseudo-classe `:hover` para aumentar a `width` (largura) desses elementos para `100%` ao passar o mouse e anime a transição usando `transition`.

Aqui está um trecho de código de exemplo:

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
