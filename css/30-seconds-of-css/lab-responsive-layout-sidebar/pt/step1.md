# Layout Responsivo com Barra Lateral (Sidebar)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um layout responsivo com uma área de conteúdo e uma barra lateral, use `display: grid` no contêiner pai, `minmax()` para a segunda coluna (barra lateral) para permitir que ela ocupe entre `150px` e `20%`, e `1fr` para a primeira coluna (conteúdo principal) para ocupar o restante do espaço disponível. Aqui está um exemplo de código HTML e CSS:

```html
<div class="container">
  <main>Este elemento tem 1fr de largura.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
