# 제어되지 않는 Textarea 요소

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 부모 컴포넌트에 의해 제어되지 않는 `<textarea>` 요소를 렌더링합니다. 콜백 함수를 사용하여 입력 값을 부모 컴포넌트로 전달합니다.

이 함수를 사용하려면:

- 부모 컴포넌트에서 `defaultValue` prop 을 입력 필드의 초기 값으로 전달합니다.
- `onChange` 이벤트를 사용하여 `onValueChange` 콜백을 트리거하고 새 값을 부모에게 보냅니다.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

사용 예시:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
