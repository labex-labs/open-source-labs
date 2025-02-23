# Обрезание многострочного текста

> Вы можете написать код в `index.html` и `style.css`..

Ограничьте многострочный текст заданным количеством строк.

- Используйте `-webkit-line-clamp`, чтобы установить максимальное количество строк для отображения.
- Установите `display` в `-webkit-box`, а `-webkit-box-orient` в `vertical`, так как они необходимы для применения `-webkit-line-clamp`.
- Примените `overflow: hidden`, чтобы скрыть любое переполнение после обрезания текста.

```html
<p class="excerpt">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod enim
  eget ultricies sollicitudin. Nunc aliquam arcu arcu, non suscipit metus luctus
  id. Aliquam sodales turpis ipsum, in vehicula dui tempor sit amet. Nullam quis
  urna erat. Pellentesque mattis dolor purus. Aliquam nisl urna, tempor a
  euismod a, placerat in mauris. Phasellus neque quam, dapibus quis nunc at,
  feugiat suscipit tortor. Duis vel posuere dolor. Phasellus risus erat,
  lobortis et mi vel, viverra faucibus lectus. Etiam ut posuere sapien. Nulla
  ultrices dui turpis, interdum consectetur urna tempus at.
</p>
```

```css
.excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```
