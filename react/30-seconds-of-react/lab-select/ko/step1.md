# 제어되지 않는 Select 요소

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이것은 제어되는 `<select>` 요소를 렌더링하는 컴포넌트입니다. 이 컴포넌트는 값의 배열과 선택된 값을 부모 컴포넌트로 전달하는 콜백 함수를 받습니다. 이 컴포넌트를 사용하는 단계는 다음과 같습니다.

- `selectedValue` prop 을 사용하여 `<select>` 요소의 초기 값을 설정합니다.
- `<select>` 요소의 값이 변경될 때 호출되어야 하는 콜백 함수를 지정하기 위해 `onValueChange` prop 을 사용합니다.
- 전달된 각 값에 대한 `<option>` 요소를 생성하기 위해 `values` 배열에 `Array.prototype.map()`을 사용합니다.
- `values`의 각 항목은 2 개의 요소 배열이어야 합니다. 여기서 첫 번째 요소는 항목의 `value`이고 두 번째 요소는 표시될 텍스트입니다.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

이 컴포넌트를 사용하는 방법의 예는 다음과 같습니다.

```jsx
const choices = [
  ["grapefruit", "Grapefruit"],
  ["lime", "Lime"],
  ["coconut", "Coconut"],
  ["mango", "Mango"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
