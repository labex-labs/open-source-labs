# Floating Section Headings in a List

To create a list with floating section headings for each section, follow these steps:

1. Add the code in `index.html` and `style.css`.

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

2. Use `overflow-y: auto` to allow the list container to overflow vertically.

```css
.floating-stack {
  overflow-y: auto;
}
```

3. Use `display: grid` on the inner container (`<dl>`) to create a layout with two columns.

```css
.floating-stack > dl {
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}
```

4. Set headings (`<dt>`) to `grid-column: 1` and content (`<dd>`) to `grid-column: 2`.

```css
.floating-stack dt {
  grid-column: 1;
}

.floating-stack dd {
  grid-column: 2;
}
```

5. Finally, apply `position: sticky` and `top: 0.5rem` to headings to create a floating effect.

```css
.floating-stack dt {
  position: sticky;
  top: 0.5rem;
}
```

This will create a list with floating section headings for each section.
