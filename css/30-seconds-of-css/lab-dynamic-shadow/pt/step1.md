# Sombra Dinâmica

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma sombra que seja baseada nas cores de um elemento, siga estes passos:

1. Use o pseudo-elemento `::after` com `position: absolute` e `width` e `height` definidos para `100%` para preencher o espaço disponível no elemento pai.

2. Herde o `background` (fundo) do elemento pai usando `background: inherit`.

3. Desloque ligeiramente o pseudo-elemento usando `top`. Em seguida, use `filter: blur()` para criar uma sombra e defina `opacity` (opacidade) para torná-la semi-transparente.

4. Posicione o pseudo-elemento atrás de seu pai definindo `z-index: -1`. Defina `z-index: 1` no elemento pai.

Aqui está um exemplo de código HTML e CSS:

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
