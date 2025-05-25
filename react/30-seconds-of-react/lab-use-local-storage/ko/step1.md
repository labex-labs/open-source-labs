# React useLocalStorage 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 `localStorage`에 저장되는 값과 이를 수정하는 함수를 생성합니다. 작동 방식은 다음과 같습니다.

1. 값을 생성하려면, 초기화를 지연시키는 함수와 함께 `useState()` 훅을 사용합니다.
2. `localStorage`에서 저장된 값을 검색하려면 `try...catch` 블록과 `Storage.getItem()`을 사용합니다. 저장된 값이 없으면 `Storage.setItem()`을 사용하여 `defaultValue`를 저장하고 이를 초기 상태로 사용합니다. 오류가 발생하면 `defaultValue`를 사용합니다.
3. 전달된 값으로 상태 변수를 업데이트하고 `Storage.setItem()`을 사용하여 저장하는 함수를 정의합니다.

다음은 코드입니다.

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

이 함수는 다음과 같이 앱에서 사용할 수 있습니다.

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
