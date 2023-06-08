# List With Floating Section Headings

`index.html` and `style.css` have already been provided in the VM.

To create a list with floating headings for each section, follow these steps:

1. Apply `overflow-y: auto` to the list container to allow for vertical overflow.
2. Use `display: grid` on the inner container (`<dl>`) to create a layout with two columns.
3. Set headings (`<dt>`) to `grid-column: 1` and content (`<dd>`) to `grid-column: 2`.
4. Finally, apply `position: sticky` and `top: 0.5rem` to headings to create a floating effect.

Here is the HTML code:

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

And here is the CSS code:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455A64;
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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
