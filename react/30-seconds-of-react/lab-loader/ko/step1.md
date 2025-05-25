# 회전 로더

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

**회전 로더 컴포넌트를 렌더링합니다.**

회전 로더 컴포넌트를 렌더링하려면 다음 단계를 따르세요.

1. `size` prop 에 의해 치수가 결정되는 SVG 요소를 렌더링합니다.
2. CSS 를 사용하여 SVG 에 애니메이션을 적용하여 회전 애니메이션을 만듭니다. 구체적으로, `.loader` 클래스를 SVG 에 추가하고 `animation` 속성을 `rotate 2s linear infinite`로 설정합니다. 또한 SVG 를 360 도 회전시키는 `transform` 속성을 사용하여 `rotate` keyframes 를 정의합니다.
3. 회전하는 원을 나타내는 `circle` 요소를 SVG 에 추가합니다. 원에 애니메이션을 적용하려면 `.loader circle` 선택자를 추가하고 `animation` 속성을 `dash 1.5s ease-in-out infinite`로 설정합니다. 또한 원 주위를 이동하는 점선 패턴을 만드는 `stroke-dasharray` 및 `stroke-dashoffset` 속성을 사용하여 `dash` keyframes 를 정의합니다.
4. 마지막으로, 너비와 높이 속성으로 전달된 `size` prop 을 사용하여 SVG 를 렌더링하는 `Loader` 컴포넌트를 만듭니다.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

`Loader` 컴포넌트를 크기 24 로 사용하려면 `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`를 호출합니다.

웹 서비스를 포트 8080 에서 실행하려면 오른쪽 하단의 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
