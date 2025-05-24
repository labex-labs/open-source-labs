# Lista com Faixas Zebradas

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma lista com cores de fundo alternadas, use os seletores de pseudo-classe `:nth-child(odd)` ou `:nth-child(even)` para aplicar um `background-color` diferente aos elementos com base em sua posição entre os irmãos. Isso pode ser aplicado a vários elementos HTML, como `<div>`, `<tr>`, `<p>`, `<ol>`, etc.

Aqui está um exemplo de como criar uma lista com faixas usando elementos `<li>`:

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
