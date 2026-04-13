from collections import Counter

# だめ回答
# # 同一個数の要素があるときに上書きしちゃっている!
# # count_to_values になるんだなー｡｡｡うーん､考慮できてなかった｡swapという名前に引きづられた｡

def get_count_to_values(d: dict)->dict:
    swapped = dict()
    for k, v in d.items():
        if v not in swapped:
            swapped[v] = []
        swapped[v].append(k)
    return swapped

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        # print(num_to_count)        
        count_to_nums = get_count_to_values(num_to_count)
        # print(count_to_num)
        count_to_nums = dict(sorted(count_to_nums.items(), reverse=True))
        top_k_nums = []
        print(count_to_nums)
        for count, nums in count_to_nums.items():
            for num in nums:
                top_k_nums.append(num)
        return top_k_nums[:k]
        # 選択肢｡valuesを開きながらtop_kに入れていくか､vluesを全部開いて､top_kに入れていくか
        # while len(top_k_nums) < k:
        #     if i > len(count_to_num):
        #         break
        #     # print(f"{i=}, {count_to_num[i][0]=}, {count_to_num[i][1]=}")
        #     top_k_nums.append(count_to_num[i][1])
        # return top_k_nums


# # だめ回答
# # 同一個数の要素があるときに上書きしちゃっている!
# # count_to_values になるんだなー｡｡｡うーん､考慮できてなかった｡swapという名前に引きづられた｡

# def swap_key_value(d: dict)->dict:
#     swapped = dict()
#     for k, v in d.items():
#         swapped[v] = k
#     return swapped

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         num_to_count = Counter(nums)
#         print(num_to_count)        
#         count_to_num = swap_key_value(num_to_count)
#         print(count_to_num)
#         count_to_num = list(sorted(count_to_num.items(), reverse=True))
#         top_k_nums = []
#         print(count_to_num)
#         for i in range(k):
#             if i > len(count_to_num):
#                 break
#             print(f"{i=}, {count_to_num[i][0]=}, {count_to_num[i][1]=}")
#             top_k_nums.append(count_to_num[i][1])
#         return top_k_nums
            
"""
アプローチ
- countして､要素数でソート
- heapでうまいことやる方法もあった気がする

- d.items()[0] で起きていること
    - items() で見ているものは [0] ができる!
- そろそろ､sorted() の中身が気になる｡

- kとlen(nums) の大小のエッジケース
    - k = len(nums) のとき､kが一つデカくなる｡

- 変数名
    - key_to_value を書くと､
    - key_to_value_sorted
    - key_to_value_tuple 
    とかしたくなるが､迷彩になりやすい｡
"""