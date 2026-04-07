func groupAnagrams(strs []string) [][]string {
    char_freq_set := make(map[[26]int][]string)

    for _, word := range strs {
        var char_freq [26]int
        for _, char := range word {
            char_freq[char - 'a']++
        }
        char_freq_set[char_freq] = append(char_freq_set[char_freq], word)
    }

    result := make([][]string, 0, len(char_freq_set))
    for _, value := range char_freq_set {
        result = append(result, value)
    }
    return result
}
