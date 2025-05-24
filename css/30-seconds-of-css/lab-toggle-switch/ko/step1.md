# 토글 스위치

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

다음은 내용의 더 간결하고 명확한 버전입니다.

CSS 만 사용하여 토글 스위치를 만들려면 다음 단계를 따르세요.

1. `for` 속성을 사용하여 `<label>`을 체크박스 `<input>` 요소와 연결합니다.
2. 스위치에 대한 원형 노브를 생성하기 위해 `<label>`의 `::after` 의사 요소를 사용합니다.
3. `:checked` 의사 클래스 선택자를 사용하여 `transform: translateX(20px)` 및 스위치의 `background-color`를 사용하여 노브의 위치를 변경합니다.
4. `position: absolute` 및 `left: -9999px`를 사용하여 `<input>` 요소를 시각적으로 숨깁니다.

다음은 HTML 코드입니다.

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

다음은 CSS 코드입니다.

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
