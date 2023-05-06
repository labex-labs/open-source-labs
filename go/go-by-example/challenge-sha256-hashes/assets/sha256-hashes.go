
s := "sha256 this string"
h := sha256.New()
h.Write([]byte(s))
bs := h.Sum(nil)
fmt.Println(s)
fmt.Printf("%x\n", bs) // TODO: Print the SHA256 hash of the string
