# React usePersistedState Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

이 훅은 `localStorage`에 지속적으로 저장되는 상태 값과 함께 이를 업데이트하는 데 사용할 수 있는 함수를 반환합니다. 사용하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 `value`를 `defaultValue`로 초기화합니다.
2. `useRef()` 훅을 사용하여 `Window.localStorage`에 있는 값의 `name`을 저장할 ref 를 생성합니다.
3. 초기화, `value` 변경, `name` 변경을 위해 각각 `useEffect()` 훅의 3 개 인스턴스를 사용합니다.
4. 컴포넌트가 처음 마운트될 때, 저장된 값이 있으면 `Storage.getItem()`을 사용하여 `value`를 업데이트하고, 그렇지 않으면 `Storage.setItem()`을 사용하여 현재 값을 지속적으로 저장합니다.
5. `value`가 업데이트되면 `Storage.setItem()`을 사용하여 새 값을 저장합니다.
6. `name`이 업데이트되면 `Storage.setItem()`을 사용하여 새 키를 생성하고, `nameRef`를 업데이트하며, `Storage.removeItem()`을 사용하여 이전 키를 `Window.localStorage`에서 제거합니다.
7. 이 훅은 기본 값 (예: 객체가 아닌) 과 함께 사용하도록 설계되었으며, 다른 코드에 의한 `Window.localStorage` 변경 사항은 고려하지 않습니다. 이 두 가지 문제는 쉽게 처리할 수 있습니다 (예: JSON 직렬화 및 `'storage'` 이벤트 처리).

다음은 코드입니다.

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
