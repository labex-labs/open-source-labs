# _Checkbox_ Personalizada

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma _checkbox_ estilizada com animação na mudança de estado:

1.  Crie um símbolo de verificação como um elemento `<svg>` com um elemento `<symbol>` dentro. Use o elemento `<use>` para inseri-lo como um ícone SVG reutilizável.
2.  Crie uma `div` container com a classe `.checkbox-container`. Use _flexbox_ para criar o _layout_ apropriado para as _checkboxes_.
3.  Oculte o elemento `<input>` e associe um _label_ a ele para exibir uma _checkbox_ e o texto fornecido.
4.  Para animar o símbolo de verificação na mudança de estado, use `stroke-dashoffset`.
5.  Para criar um efeito de animação de zoom, use `transform: scale(0.9)` via uma animação CSS.

HTML:

```html
<svg class="checkbox-symbol">
  <symbol id="check" viewbox="0 0 12 10">
    <polyline
      points="1.5 6 4.5 9 10.5 1"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
    ></polyline>
  </symbol>
</svg>

<div class="checkbox-container">
  <input class="checkbox-input" id="apples" type="checkbox" />
  <label class="checkbox" for="apples">
    <span>
      <svg width="12px" height="10px">
        <use xlink:href="#check"></use>
      </svg>
    </span>
    <span>Apples</span>
  </label>
  <input class="checkbox-input" id="oranges" type="checkbox" />
  <label class="checkbox" for="oranges">
    <span>
      <svg width="12px" height="10px">
        <use xlink:href="#check"></use>
      </svg>
    </span>
    <span>Oranges</span>
  </label>
</div>
```

CSS:

```css
.checkbox-symbol {
  position: absolute;
  width: 0;
  height: 0;
  pointer-events: none;
  user-select: none;
}

.checkbox-container {
  box-sizing: border-box;
  background: #ffffff;
  color: #222;
  height: 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: row wrap;
}

.checkbox-container * {
  box-sizing: border-box;
}

.checkbox-input {
  position: absolute;
  visibility: hidden;
}

.checkbox {
  user-select: none;
  cursor: pointer;
  padding: 6px 8px;
  border-radius: 6px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
}

.checkbox:not(:last-child) {
  margin-right: 6px;
}

.checkbox:hover {
  background: rgba(0, 119, 255, 0.06);
}

.checkbox span {
  vertical-align: middle;
  transform: translate3d(0, 0, 0);
}

.checkbox span:first-child {
  position: relative;
  flex: 0 0 18px;
  width: 18px;
  height: 18px;
  border-radius: 4px;
  transform: scale(1);
  border: 1px solid #cccfdb;
  transition: all 0.3s ease;
}

.checkbox span:first-child svg {
  position: absolute;
  top: 3px;
  left: 2px;
  fill: none;
  stroke: #fff;
  stroke-dasharray: 16px;
  stroke-dashoffset: 16px;
  transition: all 0.3s ease;
  transform: translate3d(0, 0, 0);
}

.checkbox span:last-child {
  padding-left: 8px;
  line-height: 18px;
}

.checkbox:hover span:first-child {
  border-color: #0077ff;
}

.checkbox-input:checked + .checkbox span:first-child {
  background: #0077ff;
  border-color: #0077ff;
  animation: zoom-in-out 0.3s ease;
}

.checkbox-input:checked + .checkbox span:first-child svg {
  stroke-dashoffset: 0;
}

@keyframes zoom-in-out {
  50% {
    transform: scale(0.9);
  }
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
