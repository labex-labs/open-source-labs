# Animação de Sublinhado ao Passar o Mouse (Hover Underline Animation)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito de sublinhado animado quando o usuário passa o mouse sobre o texto, siga estes passos:

1. Use `display: inline-block` para fazer com que o sublinhado ocupe apenas a largura do conteúdo do texto.
2. Use o pseudo-elemento `::after` com `width: 100%` e `position: absolute` para colocá-lo abaixo do conteúdo.
3. Use `transform: scaleX(0)` para inicialmente esconder o pseudo-elemento.
4. Use o seletor de pseudo-classe `:hover` para aplicar `transform: scaleX(1)` e exibir o pseudo-elemento ao passar o mouse.
5. Anime `transform` usando `transform-origin: left` e uma `transition` apropriada.
6. Remova a propriedade `transform-origin` para fazer com que a transformação se origine do centro do elemento.

Aqui está um exemplo de código HTML para aplicar o efeito a um elemento de texto:

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

E aqui está o código CSS correspondente:

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
