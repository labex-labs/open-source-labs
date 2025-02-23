#Динамическая тень

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать тень, основанную на цветах элемента, следуйте шагам:

1. Используйте псевдо-элемент `::after` с `position: absolute` и `width` и `height`, установленными в `100%`, чтобы заполнить доступное пространство в родительском элементе.

2. Наследуйте `background` родительского элемента, используя `background: inherit`.

3. Немного смещайте псевдо-элемент с использованием `top`. Затем используйте `filter: blur()` для создания тени и установите `opacity`, чтобы сделать ее полупрозрачной.

4. Разместите псевдо-элемент позади своего родителя, установив `z-index: -1`. Установите `z-index: 1` на родительском элементе.

Вот пример кода HTML и CSS:

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
