# Flexbox Centering (Flexbox 중앙 정렬)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

flexbox 를 사용하여 부모 요소 내에서 자식 요소를 수평 및 수직으로 중앙 정렬하려면 다음 단계를 따르세요.

1. 부모 요소의 `display` 속성을 `flex`로 설정하여 flexbox 레이아웃을 만듭니다.
2. `justify-content` 속성을 사용하여 자식 요소를 수평으로 중앙 정렬합니다. 값을 `center`로 설정합니다.
3. `align-items` 속성을 사용하여 자식 요소를 수직으로 중앙 정렬합니다. 값을 `center`로 설정합니다.
4. 부모 요소 내에 자식 요소를 추가합니다.

다음은 코드 스니펫 예시입니다.

```html
<div class="flexbox-centering">
  <div>Centered content.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
