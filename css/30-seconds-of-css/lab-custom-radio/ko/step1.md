# 사용자 정의 라디오 버튼

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

상태 변경 시 애니메이션이 적용된 스타일 지정된 라디오 버튼을 만들려면 다음 단계를 따르세요.

1. flexbox 를 사용하여 라디오 버튼에 적절한 레이아웃을 생성하기 위해 `.radio-container`를 만듭니다.
2. `<input>`의 스타일을 재설정하고 이를 사용하여 라디오 버튼의 윤곽선과 배경을 만듭니다.
3. `::before` 요소를 사용하여 라디오 버튼의 내부 원을 만듭니다.
4. `transform: scale(1)` 및 CSS transition 을 사용하여 상태 변경 시 애니메이션 효과를 만듭니다.

다음은 HTML 코드 조각의 예입니다.

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

다음은 해당 CSS 입니다.

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
