# React useEffectOnce 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

아래 코드는 `when` 조건이 참이 될 때 `callback`을 한 번만 실행하는 함수 `useEffectOnce(callback, when)`을 구현합니다.

이 함수를 구현하려면:

- `useRef()` 훅을 사용하여 `hasRunOnce` 변수를 생성하여 이펙트의 실행 상태를 추적합니다.
- `when` 조건이 변경될 때만 실행되는 `useEffect()` 훅을 사용합니다.
- `useEffect()` 훅 내부에서 `when`이 `true`이고 이펙트가 이전에 실행되지 않았는지 확인합니다. 둘 다 `true`이면 `callback`을 실행하고 `hasRunOnce`를 `true`로 설정합니다.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

다음은 `useEffectOnce()`의 사용 예시입니다.

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

이 예제에서 `useEffectOnce()`는 버튼을 처음 클릭했을 때 콘솔에 "mounted"를 기록하는 데 사용됩니다. `useEffectOnce()` 훅에는 두 개의 인수가 전달됩니다: 실행할 `callback`과 확인할 `when` 조건입니다. `when` 조건은 `clicked` 상태로 설정되므로 `callback`은 `clicked`가 처음으로 `true`일 때만 실행됩니다.

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
