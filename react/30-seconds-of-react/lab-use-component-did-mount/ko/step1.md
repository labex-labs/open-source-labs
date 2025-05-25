# React useComponentDidMount 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

컴포넌트가 마운트된 직후 콜백 함수를 실행하려면 두 번째 인수로 빈 배열을 사용하여 `useEffect()` 훅을 사용할 수 있습니다. 이렇게 하면 제공된 콜백이 컴포넌트가 마운트될 때 한 번만 실행되도록 보장합니다. 아래에 표시된 `useComponentDidMount()` 함수는 이 훅을 사용하여 클래스 컴포넌트의 `componentDidMount()` 라이프사이클 메서드와 동일한 동작을 구현합니다.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
