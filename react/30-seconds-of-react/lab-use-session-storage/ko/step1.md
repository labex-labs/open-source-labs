# React useSessionStorage 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

`sessionStorage`에 지속적으로 저장되는 상태 값과 이를 업데이트하는 함수를 만들려면 다음 단계를 따르세요.

1. 값을 지연 초기화하는 함수와 함께 `useState()` 훅을 사용합니다.
2. `try...catch` 블록과 `Storage.getItem()`을 사용하여 `Window.sessionStorage`에서 값을 가져오려고 시도합니다. 값이 없으면 `Storage.setItem()`을 사용하여 `defaultValue`를 저장하고 초기 상태로 사용합니다. 오류가 발생하면 `defaultValue`를 초기 상태로 사용합니다.
3. 전달된 값으로 상태 변수를 업데이트하고 `Storage.setItem()`을 사용하여 저장하는 함수를 정의합니다.

다음은 구현 예시입니다.

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

이 훅은 다음과 같이 앱에서 사용할 수 있습니다.

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
