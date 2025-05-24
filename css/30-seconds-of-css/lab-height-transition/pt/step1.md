# Transição de Altura (Height Transition)

`index.html` e `style.css` já foram fornecidos na VM.

Este trecho de código faz a transição da altura de um elemento de `0` para `auto` quando sua altura é desconhecida, executando as seguintes etapas:

- Use a propriedade `transition` para especificar que as mudanças em `max-height` devem ser transicionadas ao longo de uma duração de `0.3s`.
- Use a propriedade `overflow` definida como `hidden` para evitar que o conteúdo do elemento oculto transborde seu contêiner.
- Use a propriedade `max-height` para especificar uma altura inicial de `0`.
- Use a pseudo-classe `:hover` para alterar o `max-height` para o valor da variável `--max-height` definida por JavaScript.
- Use a propriedade `Element.scrollHeight` e o método `CSSStyleDeclaration.setProperty()` para definir o valor de `--max-height` para a altura atual do elemento.
- **Nota:** Essa abordagem causa reflow em cada frame de animação, o que pode causar lentidão quando há um grande número de elementos abaixo do elemento em transição.

```html
<div class="trigger">
  Passe o mouse sobre mim para ver uma transição de altura.
  <div class="el">Conteúdo adicional</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
