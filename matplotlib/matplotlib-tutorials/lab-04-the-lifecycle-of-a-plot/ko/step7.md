# 플롯 저장

마지막으로, 플롯을 디스크에 저장할 수 있습니다. 다음 단계를 따르세요.

1. `print(fig.canvas.get_supported_filetypes())`를 사용하여 지원되는 파일 형식을 출력합니다.

```python
print(fig.canvas.get_supported_filetypes())
```

2. `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`를 사용하여 그림을 이미지 파일로 저장합니다. 그림을 저장하려면 이 줄의 주석 처리를 해제하세요.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

왼쪽 사이드바의 파일 탐색기를 사용하여 저장된 이미지 파일을 열 수 있습니다.
