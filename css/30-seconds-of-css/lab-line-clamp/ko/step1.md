# 여러 줄 텍스트 자르기

> `index.html` 및 `style.css`에 코드를 작성할 수 있습니다.

여러 줄의 텍스트를 지정된 줄 수로 제한합니다.

- `-webkit-line-clamp`를 사용하여 표시할 최대 줄 수를 설정합니다.
- `-webkit-line-clamp`를 적용하려면 `display`를 `-webkit-box`로, `-webkit-box-orient`를 `vertical`로 설정해야 합니다.
- 텍스트가 잘린 후 오버플로우를 숨기기 위해 `overflow: hidden`을 적용합니다.

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
