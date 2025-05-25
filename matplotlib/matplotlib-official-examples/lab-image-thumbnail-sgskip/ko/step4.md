# 디렉토리 확인 (Verify Directory)

이 단계에서는 지정된 디렉토리가 존재하는지 확인합니다. 디렉토리가 존재하지 않으면 프로그램을 종료하고 오류 메시지를 출력합니다.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
