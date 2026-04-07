func topKFrequent(nums []int, k int) []int {
    freqMap := make(map[int]int)

    for _, num := range nums {
        freqMap[num]++
    }

    buckets := make([][]int, len(nums)+1)

    for key, value := range freqMap {
        buckets[value] = append(buckets[value], key)  
    }

    result := make([]int, 0, k)

    for i:=len(buckets)-1; i>=0; i-- {
        for _, numKey := range buckets[i] {
            result = append(result, numKey)
            if len(result) == k {
                return result
            }

        }
    }
    return result
}
