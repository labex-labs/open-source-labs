# Introdução

Neste laboratório, aprenderemos como criar um Hook React personalizado chamado `useOnWindowResize` que executará um callback sempre que a janela for redimensionada. Usaremos os Hooks `useRef()` e `useEffect()` para escutar o evento `'resize'` do objeto global `Window` e fazer a limpeza quando o componente for desmontado. Este Hook pode ser útil para criar aplicações web responsivas que precisam se ajustar a diferentes tamanhos de tela.
