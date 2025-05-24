# Focus Within (포커스 내부)

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

자식 요소 중 하나라도 포커스를 받으면 양식의 모양을 변경하려면 `:focus-within` 가상 클래스를 사용하여 부모 요소에 스타일을 적용합니다. 예를 들어, 주어진 HTML 코드에서 입력 필드 중 하나라도 포커스를 받으면 `form` 요소는 녹색 배경을 갖게 됩니다. 자식 요소에 스타일을 적용하려면 `label` 및 `input`과 같은 적절한 CSS 선택자를 사용하십시오.

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
