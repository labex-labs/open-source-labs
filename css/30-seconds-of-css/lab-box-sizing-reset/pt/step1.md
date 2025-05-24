# Box-Sizing Reset

`index.html` e `style.css` já foram fornecidos na VM.

Para garantir que a `width` (largura) e a `height` (altura) de um elemento não sejam afetadas por `border` (borda) ou `padding` (preenchimento), use a propriedade CSS `box-sizing: border-box`. Isso inclui o `padding` e a `border` no cálculo da `width` e `height` do elemento. Se você deseja herdar a propriedade `box-sizing` de um elemento pai, use `box-sizing: inherit`.

Aqui está um exemplo de como usar a propriedade `box-sizing` com dois elementos `div`:

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

Neste exemplo, o primeiro elemento `div` tem `box-sizing: border-box`, e o segundo elemento `div` tem `box-sizing: content-box`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
