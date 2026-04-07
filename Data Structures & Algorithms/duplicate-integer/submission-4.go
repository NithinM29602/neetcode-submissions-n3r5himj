func hasDuplicate(nums []int) bool {
    var unique_set []int
    for _, num := range nums{
        for _, seen := range unique_set {
            if seen == num{
                return true
            }
        }
        unique_set = append(unique_set, num)
    }
    return false
}
