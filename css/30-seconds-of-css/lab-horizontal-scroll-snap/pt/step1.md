# _Scroll Snap_ Horizontal

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um contêiner com rolagem horizontal que se encaixa em elementos durante a rolagem, siga estes passos:

1.  Use `display: grid` e `grid-auto-flow: column` para criar um layout horizontal.
2.  Use `scroll-snap-type: x mandatory` e `overscroll-behavior-x: contain` para criar um efeito de encaixe na rolagem horizontal.
3.  Altere `scroll-snap-align` para `start`, `stop` ou `center` para ajustar o alinhamento do encaixe.

Aqui está um exemplo de código HTML e CSS que você pode usar:

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
