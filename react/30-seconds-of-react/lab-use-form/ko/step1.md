# React useForm 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

폼 필드에서 상태 값을 생성하려면 `useState()` 훅을 사용하여 폼의 값에 대한 상태 변수를 생성할 수 있습니다. 그런 다음, 폼 필드에서 트리거된 적절한 이벤트를 기반으로 상태 변수를 업데이트하는 함수를 생성합니다.

다음은 예시 구현입니다.

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

위의 예에서 `useForm()`은 초기 상태 객체를 받아 `useState()`를 사용하여 `values` 상태 변수를 생성하고, `values`와 전달된 이벤트를 기반으로 `values`를 업데이트하는 함수를 포함하는 배열을 반환합니다.

다음과 같이 폼 컴포넌트에서 `useForm()`을 사용할 수 있습니다.

```jsx
const Form = () => {
  const initialState = { email: "", password: "" };
  const [values, setValues] = useForm(initialState);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" onChange={setValues} />
      <input type="password" name="password" onChange={setValues} />
      <button type="submit">Submit</button>
    </form>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

`Form` 컴포넌트에서 `useForm()`은 초기 상태 객체와 함께 호출되어 `values`와 `setValues()`를 포함하는 배열을 반환합니다. `handleSubmit()` 함수는 폼이 제출될 때 `values` 객체를 콘솔에 기록합니다. `input` 요소는 `setValues()` 함수를 사용하여 폼 값을 업데이트하도록 설정됩니다.

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
