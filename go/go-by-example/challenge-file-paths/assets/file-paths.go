
// TODO: Use Join to construct a path from the given directory and file name.
path := filepath.Join("dir", "file")

// TODO: Use Dir and Base to split the path into directory and file components.
dir := filepath.Dir(path)
file := filepath.Base(path)

// TODO: Use IsAbs to check whether the path is absolute.
isAbs := filepath.IsAbs(path)

// TODO: Use Ext to find the extension of the file.
ext := filepath.Ext(path)

// TODO: Use TrimSuffix to remove the extension from the file name.
name := strings.TrimSuffix(file, ext)

// TODO: Use Rel to find a relative path between the two paths.
rel, err := filepath.Rel("a/b", "a/b/t/file")
if err != nil {
    panic(err)
}
