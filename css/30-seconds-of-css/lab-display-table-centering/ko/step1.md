# Display Table 가운데 정렬

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

자식 요소를 부모 요소 내에서 수직 및 수평으로 모두 가운데 정렬하려면 다음 단계를 따르세요.

1. 고정된 `height` 및 `width`를 가진 컨테이너 요소를 추가합니다.

```html
<div class="container"></div>
```

2. 컨테이너 요소 안에 자식 요소를 추가하고 `.center` 클래스를 지정합니다.

```html
  <div class="center"><span>Centered content</span></div>
</div>
```

3. CSS 에서 컨테이너 요소에 다음 스타일을 적용합니다.

- `height` 및 `width`를 원하는 고정 값으로 설정합니다.
- 테두리를 추가합니다 (선택 사항).

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. CSS 에서 자식 요소에 다음 스타일을 적용합니다.

- `.center` 요소가 `<table>` 요소처럼 동작하도록 `display: table`을 사용합니다.
- 요소가 부모 요소 내에서 사용 가능한 공간을 채우도록 `height` 및 `width`를 `100%`로 설정합니다.
- 자식 요소가 `<td>` 요소처럼 동작하도록 자식 요소에 `display: table-cell`을 사용합니다.
- 자식 요소를 수평 및 수직으로 가운데 정렬하기 위해 자식 요소에 `text-align: center` 및 `vertical-align: middle`을 사용합니다.

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
