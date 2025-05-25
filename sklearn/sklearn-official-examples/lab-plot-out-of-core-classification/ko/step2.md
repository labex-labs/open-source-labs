# Reuters 문서 스트림 정의

```python
def stream_reuters_documents(data_path=None):
    """Reuters 데이터셋의 문서들을 반복합니다.

    `data_path` 디렉토리가 존재하지 않으면 Reuters 아카이브가 자동으로 다운로드 및 압축 해제됩니다.

    문서는 'body' (문자열), 'title' (문자열), 'topics' (문자열 리스트) 키를 가진 사전으로 표현됩니다.

    """

    DOWNLOAD_URL = (
        "http://archive.ics.uci.edu/ml/machine-learning-databases/"
        "reuters21578-mld/reuters21578.tar.gz"
    )
    ARCHIVE_SHA256 = "3bae43c9b14e387f76a61b6d82bf98a4fb5d3ef99ef7e7075ff2ccbcf59f9d30"
    ARCHIVE_FILENAME = "reuters21578.tar.gz"

    if data_path is None:
        data_path = Path(get_data_home()) / "reuters"
    else:
        data_path = Path(data_path)
    if not data_path.exists():
        """데이터셋을 다운로드합니다."""
        print("데이터셋을 %s에 다운로드합니다 (한 번만)." % data_path)
        data_path.mkdir(parents=True, exist_ok=True)

        def progress(blocknum, bs, size):
            total_sz_mb = "%.2f MB" % (size / 1e6)
            current_sz_mb = "%.2f MB" % ((blocknum * bs) / 1e6)
            if _not_in_sphinx():
                sys.stdout.write("\rdownloaded %s / %s" % (current_sz_mb, total_sz_mb))

        archive_path = data_path / ARCHIVE_FILENAME

        urlretrieve(DOWNLOAD_URL, filename=archive_path, reporthook=progress)
        if _not_in_sphinx():
            sys.stdout.write("\r")

        # 아카이브가 손상되지 않았는지 확인합니다:
        assert sha256(archive_path.read_bytes()).hexdigest() == ARCHIVE_SHA256

        print("Reuters 데이터셋을 압축 해제 중...")
        tarfile.open(archive_path, "r:gz").extractall(data_path)
        print("완료.")

    parser = ReutersParser()
    for filename in data_path.glob("*.sgm"):
        for doc in parser.parse(open(filename, "rb")):
            yield doc
```
