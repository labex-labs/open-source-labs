# JSX 로 마크업 작성하기

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드만 추가하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오.

```bash
npm i
```

위에서 보신 마크업 구문은 JSX 라고 합니다. 선택 사항이지만, 대부분의 React 프로젝트는 편의성을 위해 JSX 를 사용합니다.

JSX 는 HTML 보다 더 엄격합니다. `<br />`과 같은 태그를 닫아야 합니다. 또한 컴포넌트는 여러 JSX 태그를 반환할 수 없습니다. `<h1>...</h1>` 또는 빈 `<>...</>` 래퍼와 같이 공유된 부모로 묶어야 합니다.

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

HTML 을 JSX 로 많이 포팅해야 하는 경우, [온라인 변환기](https://transform.tools/html-to-jsx)를 사용할 수 있습니다.

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
