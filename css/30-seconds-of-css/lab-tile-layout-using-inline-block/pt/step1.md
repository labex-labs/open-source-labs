# Layout de 3 Blocos

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um layout de 3 blocos, use `display: inline-block` em vez de `float`, `flex` ou `grid`. Use `width` em combinação com `calc` para dividir a largura do contêiner uniformemente em 3 colunas. Para evitar espaços em branco, defina `font-size` como `0` para `.tiles` e como `20px` para elementos `<h2>` para exibir o texto. Observe que o uso de `font-size: 0` para combater espaços em branco entre blocos pode causar efeitos colaterais se você usar unidades relativas (por exemplo, `em`).

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
