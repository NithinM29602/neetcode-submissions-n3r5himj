func groupAnagrams(strs []string) [][]string {
    var groups = make(map[string][]string)

    for _, word := range strs {

        s := strings.Split(word, "")
        sort.Strings(s)
        key := strings.Join(s, "")

        groups[key] = append(groups[key], word)
    }

    result := make([][]string, 0, len(groups))
    for _, value := range groups {
        result = append(result, value)
    }

    return result
}
