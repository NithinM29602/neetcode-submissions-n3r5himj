func longestConsecutive(nums []int) int {
    set := make(map[int]struct{})

    for _, eachNum := range nums {
        set[eachNum] = struct{}{}
    }

    longest := 0
    for eachNum := range set {
        currentStreak := 0
        if _, leftExists := set[eachNum-1]; !leftExists {
            currentStreak++
            nextItem := eachNum + 1
            for {
                if _, nextExists := set[nextItem]; nextExists {
                    nextItem++
                    currentStreak++
                } else {
                    break
                }
            }
        }

        if currentStreak > longest {
            longest = currentStreak
        }
    }
    return longest
}
