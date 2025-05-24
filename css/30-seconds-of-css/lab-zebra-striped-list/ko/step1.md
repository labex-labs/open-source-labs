# 얼룩말 무늬 목록 (Zebra Striped List)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

교대로 배경색을 가진 목록을 만들려면, `:nth-child(odd)` 또는 `:nth-child(even)` 의사 클래스 선택자 (pseudo-class selectors) 를 사용하여 형제 요소들 사이에서의 위치에 따라 다른 `background-color`를 요소에 적용합니다. 이는 `<div>`, `<tr>`, `<p>`, `<ol>` 등과 같은 다양한 HTML 요소에 적용될 수 있습니다.

`<li>` 요소를 사용하여 줄무늬 목록을 만드는 방법의 예는 다음과 같습니다.

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
