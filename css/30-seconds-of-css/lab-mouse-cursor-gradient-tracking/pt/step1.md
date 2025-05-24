# Rastreamento de Gradiente do Cursor do Mouse

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito de hover onde o gradiente segue o cursor do mouse, siga estes passos:

1.  Declare duas variáveis CSS, `--x` e `--y`, para rastrear a posição do mouse no botão.
2.  Declare uma variável CSS, `--size`, para modificar as dimensões do gradiente.
3.  Use `background: radial-gradient(circle closest-side, pink, transparent)` para criar o gradiente na posição correta.
4.  Registre um manipulador para o evento `'mousemove'` usando `Document.querySelector()` e `EventTarget.addEventListener()`.
5.  Atualize os valores das variáveis CSS `--x` e `--y` usando `Element.getBoundingClientRect()` e `CSSStyleDeclaration.setProperty()`.

Aqui está o código HTML para o botão:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

E aqui está o código CSS:

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Finalmente, aqui está o código JavaScript:

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
