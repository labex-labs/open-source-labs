# Выпадающее меню

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Для создания интерактивного выпадающего меню при наведении курсора/получении фокуса следуйте шагам:

1. В CSS используйте `left: 100%`, чтобы расположить выпадающее меню справа от родительского элемента.
2. Вместо `display: none` используйте `visibility: hidden`, чтобы скрыть выпадающее меню изначально, чтобы можно было применить переходы.
3. Примените псевдо-классовые селекторы `:hover`, `:focus` и `:focus-within` к родительскому элементу, чтобы отобразить выпадающее меню при наведении курсора/получении фокуса.
4. Используйте следующий HTML и CSS код:

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

Нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
