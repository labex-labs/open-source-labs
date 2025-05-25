# React useTitle 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

페이지의 제목을 설정하려면 `useTitle` 사용자 정의 훅을 사용할 수 있습니다. 이 훅은 `typeof`를 사용하여 `Document`가 정의되었는지 확인합니다. 정의된 경우 `useRef()` 훅을 사용하여 `Document`의 원래 제목을 저장합니다. 그런 다음 `useEffect()` 훅을 사용하여 컴포넌트가 마운트될 때 `Document.title`을 전달된 값으로 설정하고 언마운트될 때 정리합니다.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

예제 코드에서 `Alert` 컴포넌트는 `useTitle` 훅을 사용하여 제목을 "Alert"로 설정합니다. `MyApp` 컴포넌트는 `Alert` 컴포넌트를 토글하는 버튼을 렌더링합니다.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
