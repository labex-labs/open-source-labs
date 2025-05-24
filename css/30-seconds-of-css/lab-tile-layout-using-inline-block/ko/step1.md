# 3-타일 레이아웃

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

3-타일 레이아웃을 만들려면 `float`, `flex` 또는 `grid` 대신 `display: inline-block`을 사용하십시오. `width`를 `calc`와 함께 사용하여 컨테이너의 너비를 3 개의 열로 균등하게 나눕니다. 공백을 피하려면 `.tiles`에 `font-size`를 `0`으로 설정하고, 텍스트를 표시하기 위해 `<h2>` 요소에 `20px`로 설정합니다. 블록 사이의 공백을 없애기 위해 `font-size: 0`을 사용하는 것은 상대 단위 (예: `em`) 를 사용하는 경우 부작용을 일으킬 수 있습니다.

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
