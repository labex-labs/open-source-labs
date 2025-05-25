# 제어되지 않는 입력 필드

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 값 업데이트에 대해 부모에게 알리기 위해 콜백 함수를 사용하는 제어되지 않는 `<input>` 요소를 렌더링합니다. 사용 방법은 다음과 같습니다.

- `defaultValue` prop 을 사용하여 부모로부터 초기 값을 전달합니다.
- 값 업데이트를 처리하기 위해 `onValueChange`라는 콜백 함수를 전달합니다.
- `onChange` 이벤트를 사용하여 콜백을 실행하고 새 값을 부모에게 보냅니다.

다음은 예시입니다.

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
