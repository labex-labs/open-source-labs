# 다중 선택이 가능한 상태 저장 체크박스

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 체크박스 목록을 렌더링하고 콜백 함수를 사용하여 선택된 값 (value) 을 상위 컴포넌트로 보냅니다. 이를 생성하는 단계는 다음과 같습니다.

1. `useState()` 훅을 사용하여 `options` prop 으로 `data` 상태 변수를 초기화합니다.
2. 선택된 옵션 (option) 으로 `data` 상태 변수를 업데이트하고 `onChange` 콜백 함수를 호출하는 `toggle` 함수를 생성합니다.
3. `data` 상태 변수를 매핑하여 개별 체크박스와 레이블을 생성합니다. 각 체크박스의 `onClick` 핸들러에 `toggle` 함수를 바인딩합니다.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

다음은 이를 사용하는 예시입니다.

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
