# 접두사가 있는 입력

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

시각적인, 편집 불가능한 접두사가 있는 입력을 만들려면 다음 단계를 따르세요.

1. `display: flex`를 사용하여 `.input-box` 클래스가 있는 컨테이너 요소를 만듭니다.
2. `<input>` 필드에서 테두리와 윤곽선을 제거하고 대신 부모 요소에 적용하여 입력 상자처럼 보이게 합니다.
3. 사용자가 `<input>` 필드와 상호 작용할 때 `:focus-within` 의사 클래스 선택자를 사용하여 부모 요소를 적절하게 스타일링합니다.

다음은 HTML 코드입니다.

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

다음은 CSS 코드입니다.

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box .prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
