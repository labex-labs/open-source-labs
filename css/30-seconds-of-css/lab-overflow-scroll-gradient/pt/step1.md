# Gradiente de Rolagem com Overflow

`index.html` e `style.css` já foram fornecidos na VM.

Para adicionar um gradiente de desvanecimento a um elemento com overflow e indicar que há mais conteúdo para ser rolado, siga estes passos:

1.  Use o pseudo-elemento `::after` para criar um `linear-gradient()` que desvanece de `transparent` para `white` (de cima para baixo).
2.  Posicione e dimensione o pseudo-elemento em seu pai usando `position: absolute`, `width` e `height`.
3.  Exclua o pseudo-elemento de eventos de mouse usando `pointer-events: none`, permitindo que o texto atrás dele ainda seja selecionável/interativo.

Aqui está um exemplo de trecho de código HTML e CSS:

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
