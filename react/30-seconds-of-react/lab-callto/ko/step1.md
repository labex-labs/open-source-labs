# 전화 연결 링크 (Callable Telephone Link)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

전화 번호로 전화를 거는 링크를 만들려면 `Callto` 컴포넌트를 사용하십시오. 이 컴포넌트는 적절한 `href` 속성을 가진 `<a>` 요소를 생성합니다. 링크를 렌더링하려면 `phone` prop 을 사용하여 전화 번호를 지정하고, `children` prop 을 사용하여 링크 텍스트를 지정합니다.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

`Callto` 컴포넌트를 사용하려면 `ReactDOM.render()` 메서드를 호출하고 `phone` 및 `children` prop 이 설정된 `Callto` 요소를 전달합니다.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Call me!</Callto>,
  document.getElementById("root")
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
