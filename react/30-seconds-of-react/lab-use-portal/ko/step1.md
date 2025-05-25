# React usePortal 훅

> `index.html`과 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

부모 컴포넌트 외부에서 자식 요소를 렌더링하는 포털을 생성하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 포털의 `render()` 및 `remove()` 함수를 저장하는 상태 변수를 생성합니다.
2. `ReactDOM.createPortal()`과 `ReactDOM.unmountComponentAtNode()`를 사용하여 포털과 이를 제거하는 함수를 생성합니다. `useCallback()` 훅을 사용하여 이러한 함수를 `createPortal()`로 래핑하고 메모이제이션합니다.
3. `useEffect()` 훅을 사용하여 `createPortal()`을 호출하고 `el`의 값이 변경될 때마다 상태 변수를 업데이트합니다.
4. 마지막으로, 상태 변수의 `render()` 함수를 반환합니다.

다음은 예시 구현입니다.

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

이 훅을 사용하려면 원하는 DOM 요소를 인수로 사용하여 `usePortal()`을 호출하는 컴포넌트를 생성합니다. 이 컴포넌트는 반환된 `render()` 함수를 사용하여 포털에서 콘텐츠를 렌더링할 수 있습니다.

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
