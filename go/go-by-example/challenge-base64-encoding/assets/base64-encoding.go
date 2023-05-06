
// TODO: Encode the given string using standard base64 encoding
sEnc := b64.StdEncoding.EncodeToString([]byte(data))

// TODO: Decode the standard encoded string
sDec, _ := b64.StdEncoding.DecodeString(sEnc)

// TODO: Encode the given string using URL-compatible base64 encoding
uEnc := b64.URLEncoding.EncodeToString([]byte(data))

// TODO: Decode the URL-compatible encoded string
uDec, _ := b64.URLEncoding.DecodeString(uEnc)
