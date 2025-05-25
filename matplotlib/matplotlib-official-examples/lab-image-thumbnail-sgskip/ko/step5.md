# 출력 디렉토리 생성 (Create Output Directory)

이 단계에서는 썸네일이 저장될 `thumbs`라는 디렉토리를 생성합니다. 디렉토리가 이미 존재하는 경우 다시 생성되지 않습니다.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
