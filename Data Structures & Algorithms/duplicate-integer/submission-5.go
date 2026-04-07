func hasDuplicate(nums []int) bool {
    unique_set := make(map[int]bool)

    for _, num := range nums {
        if _, exists := unique_set[num]; exists {
            return true
        }
        unique_set[num] = true
    }
    return false
}
