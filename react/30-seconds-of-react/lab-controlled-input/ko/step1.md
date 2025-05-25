# 제어된 입력 필드

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드 조각은 값에 대한 업데이트를 부모에게 알리기 위해 콜백 함수를 활용하는 제어된 `<input>` 요소를 제공합니다. 작동 방식은 다음과 같습니다.

- 제어된 입력 필드의 값은 부모로부터 전달된 `value` prop 에 의해 결정됩니다.
- 사용자가 입력 필드에 변경을 가하면 `onChange` 이벤트가 캡처되어 `onValueChange` 콜백 함수를 트리거하고 새 값을 부모 컴포넌트로 다시 보냅니다.
- 입력 필드의 값을 업데이트하려면 부모가 제어된 입력 컴포넌트로 전달하는 `value` prop 을 업데이트해야 합니다.

다음은 `ControlledInput` 컴포넌트의 예시 구현과 `Form` 컴포넌트에서의 사용 예시입니다.

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
