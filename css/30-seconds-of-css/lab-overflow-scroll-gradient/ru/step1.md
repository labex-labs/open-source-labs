# Градиент прокрутки при переполнении

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы добавить затухающий градиент к элементу с переполнением и показать, что есть дополнительный контент для прокрутки, следуйте шагам:

1. Используйте псевдо-элемент `::after` для создания `linear-gradient()`, который затухает от `transparent` до `white` (сверху вниз).
2. Разместите и задайте размер псевдо-элемента в его родительском элементе с использованием `position: absolute`, `width` и `height`.
3. Исключите псевдо-элемент из событий мыши с использованием `pointer-events: none`, чтобы текст за ним по-прежнему был доступен для выбора/интерактивности.

Вот пример фрагмента кода HTML и CSS:

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

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
