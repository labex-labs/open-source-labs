# Lista com Títulos de Seção Flutuantes

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma lista com títulos flutuantes para cada seção, siga estes passos:

1.  Aplique `overflow-y: auto` ao contêiner da lista para permitir o estouro vertical.
2.  Use `display: grid` no contêiner interno (`<dl>`) para criar um layout com duas colunas.
3.  Defina os títulos (`<dt>`) para `grid-column: 1` e o conteúdo (`<dd>`) para `grid-column: 2`.
4.  Finalmente, aplique `position: sticky` e `top: 0.5rem` aos títulos para criar um efeito flutuante.

Aqui está o código HTML:

```html
<div class="container">
  <div class="floating-stack">
    <dl>
      <dt>A</dt>
      <dd>Algeria</dd>
      <dd>Angola</dd>

      <dt>B</dt>
      <dd>Benin</dd>
      <dd>Botswana</dd>
      <dd>Burkina Faso</dd>
      <dd>Burundi</dd>

      <dt>C</dt>
      <dd>Cabo Verde</dd>
      <dd>Cameroon</dd>
      <dd>Central African Republic</dd>
      <dd>Chad</dd>
      <dd>Comoros</dd>
      <dd>Congo, Democratic Republic of the</dd>
      <dd>Congo, Republic of the</dd>
      <dd>Cote d'Ivoire</dd>

      <dt>D</dt>
      <dd>Djibouti</dd>

      <dt>E</dt>
      <dd>Egypt</dd>
      <dd>Equatorial Guinea</dd>
      <dd>Eritrea</dd>
      <dd>Eswatini (formerly Swaziland)</dd>
      <dd>Ethiopia</dd>
    </dl>
  </div>
</div>
```

E aqui está o código CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
