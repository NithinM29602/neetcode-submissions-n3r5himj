func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))

    prefix := 1
    for i, value := range nums {
        res[i] = prefix
        prefix = prefix * value
    }

    suffix := 1
    for i:=len(nums)-1; i>=0; i--{
        res[i] = res[i] * suffix
        suffix = suffix * nums[i]
    }

    return res
}
