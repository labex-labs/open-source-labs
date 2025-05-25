# React useNavigatorOnLine 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

클라이언트가 온라인인지 오프라인인지 확인하려면 `Navigator.onLine` 웹 API 를 활용하는 `getOnLineStatus` 함수를 만들 수 있습니다. 그런 다음, React 컴포넌트에서 이 기능을 구현하기 위해 `useNavigatorOnLine` 사용자 정의 훅을 사용할 수 있습니다. 이 훅은 `useState()` 훅을 사용하여 `status`라는 상태 변수를 생성하고 `getOnLineStatus()`에서 반환된 값으로 설정합니다. `useEffect()` 훅은 온라인/오프라인 상태가 변경될 때 이벤트 리스너를 추가하고, 그에 따라 `status` 상태 변수를 업데이트하며, 컴포넌트가 언마운트될 때 해당 리스너를 정리하는 데 사용됩니다. 마지막으로, `useNavigatorOnLine()`에서 반환된 `isOnline` 변수를 사용하여 클라이언트가 온라인인지 오프라인인지 나타내는 메시지를 렌더링할 수 있습니다.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
