# Proporção Constante de Largura para Altura

`index.html` e `style.css` já foram fornecidos na VM.

Este trecho de código garante que um elemento com `width` variável manterá um valor de `height` proporcional. Para conseguir isso, aplique `padding-top` no pseudo-elemento `::before`, tornando a `height` do elemento igual a uma porcentagem de sua `width`. A proporção de `height` para `width` pode ser alterada conforme necessário. Por exemplo, um `padding-top` de `100%` criará um quadrado responsivo com uma proporção de 1:1. Para usar este código, basta adicionar o seguinte código HTML:

```html
<div class="constant-width-to-height-ratio"></div>
```

Em seguida, adicione o seguinte código CSS:

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
