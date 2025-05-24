# Efeito de Hover (Squiggle Link Hover Effect)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito ondulado ao passar o mouse sobre um link, você pode seguir estes passos:

1.  Crie um fundo repetitivo para o link usando um `linear-gradient`.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2.  Crie um estado `:hover` para o link com um `background-image` de uma data URL contendo um SVG com um caminho ondulado (squiggly path) e uma animação.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift .3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3.  Use o código HTML abaixo para adicionar o link à página.

```html
<p>
  The <a class="squiggle" href="#">magnificent octopus</a> swam along
  gracefully.
</p>
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
