
// Generate a random integer between 0 and 100 (inclusive)
rand.Intn(100)

// Generate a random float between 0.0 and 1.0 (exclusive)
rand.Float64()

// Generate a random float between 5.0 and 10.0 (exclusive)
(rand.Float64() * 5) + 5

// Generate a new random number generator with a seed that changes
rand.NewSource(time.Now().UnixNano())
rand.New(s1)

// Generate a new random number generator with a fixed seed
rand.NewSource(42)
rand.New(s2)
