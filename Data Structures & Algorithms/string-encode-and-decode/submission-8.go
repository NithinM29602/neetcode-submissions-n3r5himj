type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    var sr strings.Builder
    for _, eachWord := range strs {
        sr.WriteString(strconv.Itoa(len(eachWord)))
        sr.WriteByte('#')
        sr.WriteString(eachWord)
    }
    return sr.String()
}

func (s *Solution) Decode(encoded string) []string {
    var result []string

    i := 0
    for i < len(encoded) { 
        j := i

        for encoded[j] != '#' {
            j++
        }

        length, _ := strconv.Atoi(encoded[i : j])
        i = j + 1
        result = append(result, encoded[i : i + length])

        i = i + length
    }
    return result
}
