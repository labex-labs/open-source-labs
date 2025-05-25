# React useSearchParam 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

브라우저의 위치 검색 매개변수를 추적하려면 다음 단계를 따르세요.

1. `useCallback()` 훅을 사용하여 콜백을 생성합니다. 콜백은 `URLSearchParams` 생성자를 사용하여 원하는 매개변수의 현재 값을 가져와야 합니다.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. `useState()` 훅을 사용하여 매개변수의 현재 값을 저장하는 상태 변수를 생성합니다.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. `useEffect()` 훅을 사용하여 마운트 시 상태 변수를 업데이트하고 언마운트 시 정리하기 위한 적절한 이벤트 리스너를 설정합니다.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

다음은 이 사용자 지정 훅을 컴포넌트에서 사용하는 예시입니다.

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Post param value: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        View post 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Exit
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

이 예제는 `useSearchParam` 사용자 지정 훅을 사용하여 위치 검색에서 `post` 매개변수의 값을 추적하는 `MyApp` 컴포넌트를 생성합니다. `post` 값은 단락 태그에 표시됩니다. 위치 검색 매개변수 값을 변경하는 방법을 보여주기 위해 두 개의 버튼도 포함되어 있습니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
