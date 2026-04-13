func groupAnagrams(strs []string) [][]string {
    anagramGroup := make(map[string][]string)

    for _, eachWord := range strs {
        sortedWord := sortWord(eachWord)
        anagramGroup[sortedWord] = append(anagramGroup[sortedWord], eachWord)
    }

    result := [][]string{}
    for _, values := range anagramGroup {
        result = append(result, values)
    }
    return result
}

func sortWord(word string) string {
    splittedWord := strings.Split(word, "")
    sort.Strings(splittedWord)
    sortedWord := strings.Join(splittedWord, "")
    return sortedWord
}