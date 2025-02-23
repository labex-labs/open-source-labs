# Сброс размеров коробки

В ВМ уже предоставлены `index.html` и `style.css`.

Для того чтобы `width` и `height` элемента не были влияны `border` или `padding`, используйте CSS-свойство `box-sizing: border-box`. Это включает `padding` и `border` в расчете `width` и `height` элемента. Если вы хотите наследовать свойство `box-sizing` от родительского элемента, используйте `box-sizing: inherit`.

Вот пример использования свойства `box-sizing` с двумя элементами `div`:

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

В этом примере первый элемент `div` имеет `box-sizing: border-box`, а второй элемент `div` имеет `box-sizing: content-box`.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
