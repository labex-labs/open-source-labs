# 이메일 링크 (Email Link)

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 클릭 시 사용자의 이메일 클라이언트를 열고 지정된 제목과 본문 내용으로 새 이메일을 채우는 링크를 생성합니다. 링크는 `mailto:` 프로토콜을 사용하여 형식이 지정됩니다.

이 함수를 사용하려면 수신자의 이메일 주소와 함께 `email` prop 을 제공하고, 선택적으로 초기 내용으로 이메일을 채우기 위해 `subject` 및 `body` prop 을 제공합니다. 이러한 props 는 링크 URL 에 추가되기 전에 `encodeURIComponent`를 사용하여 안전하게 인코딩됩니다.

링크는 제공된 `children`을 내용으로 렌더링됩니다.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

사용 예시:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
