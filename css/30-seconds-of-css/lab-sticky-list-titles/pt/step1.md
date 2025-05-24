# Lista com Títulos de Seção Fixos

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma lista com títulos fixos para cada seção, siga estes passos:

1. Permita que o contêiner da lista (`<dl>`) transborde verticalmente usando `overflow-y: auto`.
2. Fixe os títulos (`<dt>`) no topo do contêiner definindo sua `position` como `sticky` e aplicando `top: 0`.
3. Use o seguinte código HTML e CSS:

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
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
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
