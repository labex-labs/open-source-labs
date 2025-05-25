# React useComponentWillUnmount 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

컴포넌트가 언마운트 (unmount) 되어 파괴되기 직전에 콜백을 실행하려면 두 번째 인수로 빈 배열을 사용하여 `useEffect()` 훅을 사용할 수 있습니다. 정리 (cleanup) 전에 한 번만 실행되도록 제공된 콜백을 반환합니다. 이 동작은 클래스 컴포넌트의 `componentWillUnmount()` 라이프사이클 메서드와 유사합니다. 또한 다음과 같은 코드 조각을 사용하여 `onUnmountHandler` 함수를 인수로 받아 컴포넌트가 언마운트되기 전에 실행하는 사용자 정의 훅 `useComponentWillUnmount()`를 만들 수 있습니다.

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

그런 다음 다음과 같이 이 사용자 정의 훅을 함수형 컴포넌트에서 사용할 수 있습니다.

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

이렇게 하면 컴포넌트가 언마운트되기 직전에 콘솔에 "Component will unmount"가 기록됩니다.

웹 서비스 (web service) 를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
