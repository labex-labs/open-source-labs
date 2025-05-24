# Centralização com Transformações

`index.html` e `style.css` já foram fornecidos na VM.

Para centralizar verticalmente e horizontalmente um elemento filho dentro de seu pai usando transformações CSS, siga estes passos:

1.  Defina a propriedade `position` do elemento pai como `relative` e a do elemento filho como `absolute` para posicioná-lo em relação ao seu pai.
2.  Use `left: 50%` e `top: 50%` para deslocar o elemento filho em 50% da borda esquerda e superior do elemento pai.
3.  Use `transform: translate(-50%, -50%)` para negar sua posição, de modo que ele seja centralizado tanto verticalmente quanto horizontalmente.
4.  Observe que a `height` e `width` fixas do elemento pai são apenas para fins de demonstração.

Aqui está um exemplo de código HTML:

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

E aqui está o código CSS correspondente:

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
