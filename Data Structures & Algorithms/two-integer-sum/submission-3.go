func twoSum(nums []int, target int) []int {
    two_sum_map := make(map[int]int)

    for index, num := range nums {
        complement := target - num
        if value, ok := two_sum_map[complement]; ok{
            return []int{value, index}
        }
        two_sum_map[num] = index
    }
    return nil
}
