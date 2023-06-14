# Define the stream of Reuters documents

```python
def stream_reuters_documents(data_path=None):
    """Iterate over documents of the Reuters dataset.

    The Reuters archive will automatically be downloaded and uncompressed if
    the `data_path` directory does not exist.

    Documents are represented as dictionaries with 'body' (str),
    'title' (str), 'topics' (list(str)) keys.

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
        """Download the dataset."""
        print("downloading dataset (once and for all) into %s" % data_path)
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

        # Check that the archive was not tampered:
        assert sha256(archive_path.read_bytes()).hexdigest() == ARCHIVE_SHA256

        print("untarring Reuters dataset...")
        tarfile.open(archive_path, "r:gz").extractall(data_path)
        print("done.")

    parser = ReutersParser()
    for filename in data_path.glob("*.sgm"):
        for doc in parser.parse(open(filename, "rb")):
            yield doc
```


