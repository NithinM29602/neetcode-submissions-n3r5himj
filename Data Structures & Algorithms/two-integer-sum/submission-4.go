func twoSum(nums []int, target int) []int {
    freqMap := make(map[int]int)

    for i:=0; i<len(nums); i++{
        remValue := target - nums[i]
        if value, ok := freqMap[remValue]; ok {
            return []int{value, i}
        }
        freqMap[nums[i]] = i
    }
    return nil

}
