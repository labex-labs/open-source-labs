# React useError 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 에러 디스패처를 생성합니다. 세 개의 React 훅을 사용하여 에러 상태를 관리하고 사용자 인터페이스로 디스패치합니다.

코드가 작동하는 방식은 다음과 같습니다.

1. `useState()` 훅은 에러 객체를 저장하는 `error`라는 상태 변수를 생성합니다. 이 훅은 `err`의 초기값을 인수로 받습니다.

2. `useEffect()` 훅은 truthy 할 때마다 에러를 "throw"하는 데 사용됩니다. 이 훅은 함수와 종속성 배열을 인수로 받습니다. 이 경우, 함수는 `error` 상태 변수가 truthy 한지 (즉, null, undefined, 0, false 또는 빈 문자열이 아닌지) 확인하고, truthy 하면 throw 합니다. 종속성 배열은 `[error]`이며, 이는 `error` 변수가 변경될 때마다 effect 가 다시 실행됨을 의미합니다.

3. `useCallback()` 훅은 `dispatchError`라는 캐시된 함수를 생성하는 데 사용되며, 이 함수는 `error` 상태 변수를 업데이트하고 새 함수를 반환합니다. 이 훅은 함수와 종속성 배열을 인수로 받습니다. 이 경우, 함수는 디스패치할 새 에러 객체인 `err` 인수를 받습니다. 종속성 배열은 `[]`이며, 이는 컴포넌트가 다시 렌더링될 때만 캐시된 함수가 다시 생성됨을 의미합니다.

`useError()` 훅을 컴포넌트에서 사용하는 방법의 예는 다음과 같습니다.

1. `ErrorButton`이라는 새 컴포넌트를 생성합니다.

2. 컴포넌트 내부에서 `useError()` 훅을 호출하여 `dispatchError` 함수를 가져옵니다.

3. `dispatchError`를 새 에러 객체와 함께 호출하는 `clickHandler`라는 클릭 핸들러 함수를 생성합니다.

4. 클릭 시 `clickHandler`를 호출하는 버튼을 렌더링합니다.

코드는 다음과 같습니다.

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
