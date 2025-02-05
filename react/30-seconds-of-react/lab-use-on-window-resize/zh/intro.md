# 简介

在本实验中，我们将学习如何创建一个名为 `useOnWindowResize` 的自定义 React Hook，它会在窗口大小改变时执行一个回调函数。我们将使用 `useRef()` 和 `useEffect()` Hook 来监听 `Window` 全局对象的 `'resize'` 事件，并在组件卸载时进行清理。这个 Hook 对于创建需要适应不同屏幕尺寸的响应式 Web 应用程序很有用。
