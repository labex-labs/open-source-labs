# Список с закреплёнными заголовками секций

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать список с закреплёнными заголовками для каждой секции, следуйте шагам:

1. Позволите контейнеру списка (`<dl>`) вертикально переполняться, используя `overflow-y: auto`.
2. Закрепите заголовки (`<dt>`) сверху контейнера, установив их `position` в `sticky` и применяя `top: 0`.
3. Используйте следующий HTML и CSS код:

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>Алжир</dd>
    <dd>Ангола</dd>

    <dt>B</dt>
    <dd>Бенин</dd>
    <dd>Ботсвана</dd>
    <dd>Буркина-Фасо</dd>
    <dd>Бурунди</dd>

    <dt>C</dt>
    <dd>Кабо-Верде</dd>
    <dd>Камерун</dd>
    <dd>Центральноафриканская Республика</dd>
    <dd>Чад</dd>
    <dd>Коморы</dd>
    <dd>Конго, Демократическая Республика</dd>
    <dd>Конго, Республика</dd>
    <dd>Кот-д’Ивуар</dd>

    <dt>D</dt>
    <dd>Джибути</dd>

    <dt>E</dt>
    <dd>Египет</dd>
    <dd>Экваториальная Гвинея</dd>
    <dd>Эритрея</dd>
    <dd>Эсватини (ранее Свазиленд)</dd>
    <dd>Эфиопия</dd>
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

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
