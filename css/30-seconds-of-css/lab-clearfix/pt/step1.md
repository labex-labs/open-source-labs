# Clearfix

`index.html` e `style.css` já foram fornecidos na VM.

Para garantir que um elemento se auto-limpe de seus filhos ao usar `float` para construir layouts, você pode usar o pseudo-elemento `::after` e aplicar `content: ''` para permitir que ele afete o layout. Adicionalmente, use `clear: both` para fazer com que o elemento limpe os floats esquerdo e direito. No entanto, esta técnica só funciona corretamente se não houver filhos não flutuantes no contêiner e não houver floats altos antes do contêiner com clearfix, mas no mesmo contexto de formatação (por exemplo, colunas flutuantes). Por exemplo:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

Observe que o uso de uma abordagem mais moderna, como flexbox ou grid layout, é recomendado em vez de usar `float` para construir layouts.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
