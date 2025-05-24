# Transformação de Perspectiva no Hover

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma transformação de perspectiva com uma animação de hover em um elemento:

1.  Use a propriedade `transform` com as funções `perspective()` e `rotateY()` para aplicar uma perspectiva ao elemento. Por exemplo, para criar uma perspectiva à esquerda, use `transform: perspective(1500px) rotateY(15deg);`. Para criar uma perspectiva à direita, use `transform: perspective(1500px) rotateY(-15deg);`.

2.  Use a propriedade `transition` para animar a propriedade `transform` quando o elemento estiver em hover. Por exemplo, `transition: transform 1s ease 0s;`.

3.  Para espelhar o efeito de perspectiva da esquerda para a direita, altere o valor de `rotateY()` para negativo na perspectiva direita. Por exemplo, use `transform: perspective(1500px) rotateY(-15deg);`.

Exemplo HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Exemplo CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
