
func main() {
    // TODO: Create a context with a 5-second timeout
    // TODO: Pass the context to the hello function
    // As before, we register our handler on the "/hello"
    // route, and start serving.
    http.HandleFunc("/hello", hello)
    http.ListenAndServe(":8090", nil)
}
