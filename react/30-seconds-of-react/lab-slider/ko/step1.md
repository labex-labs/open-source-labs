# 제어되지 않는 범위 입력 (Uncontrolled Range Input)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

React 에서 슬라이더를 생성하려면 `Slider` 컴포넌트를 사용하고 `min`, `max`, `defaultValue`, 및 `onValueChange` props 를 전달합니다.

`Slider` 컴포넌트에서 `<input>` 요소의 `type`을 `"range"`로 설정하여 슬라이더를 생성합니다. 상위 컴포넌트에서 전달된 `defaultValue` prop 을 제어되지 않는 입력 필드의 초기 값으로 사용합니다. `onChange` 이벤트를 사용하여 `onValueChange` 콜백을 실행하고 새 값을 상위 컴포넌트로 보냅니다.

다음은 `Slider` 컴포넌트의 코드입니다.

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

`Slider` 컴포넌트를 렌더링하려면 `ReactDOM.createRoot`를 사용하고 `onValueChange` 콜백 함수를 전달합니다.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
