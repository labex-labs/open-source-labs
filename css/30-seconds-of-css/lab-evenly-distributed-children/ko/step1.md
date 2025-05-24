# 균등하게 분산된 자식 요소

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

부모 요소 내에서 자식 요소를 균등하게 분산시키려면 부모 요소의 `display` 속성을 `flex`로 설정하여 flexbox 레이아웃을 사용합니다. 자식 요소를 가로로 균등한 간격으로 분산시키려면 `justify-content: space-between`을 사용합니다. 자식 요소를 주변에 공간을 두고 분산시키려면 `justify-content: space-around`를 사용합니다. 다음은 예시입니다.

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
