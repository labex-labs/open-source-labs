# Efeito de _Hover_ e _Focus_ para Itens de Lista de Navegação

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito personalizado de _hover_ e _focus_ para itens de navegação, use transformações CSS da seguinte forma:

1.  Use o pseudo-elemento `::before` no âncora do item da lista para criar um efeito de _hover_. Oculte-o usando `transform: scale(0)`.
2.  Use os seletores de pseudo-classe `:hover` e `:focus` para transicionar o pseudo-elemento para `transform: scale(1)` e mostrar seu fundo colorido.
3.  Evite que o pseudo-elemento cubra o elemento âncora usando `z-index`.

Você pode usar o seguinte código HTML para seu menu de navegação:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

E aplique as seguintes regras CSS:

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
