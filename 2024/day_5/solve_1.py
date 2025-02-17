from collections import defaultdict
from puzzles import text

class Solution:
    def check_page_ordering(self, text: str):
        rules, page_numbers = text.split('\n\n')
        rules_dict = defaultdict(list)
        sorted_pages = []

        for rule in rules.split('\n'):
            key, val = map(int, rule.split('|'))
            rules_dict[key].append(val)

        for row in page_numbers.split('\n'):
            row_nums = list(map(int, row.split(',')))
            is_sorted = True
            for num in range(len(row_nums)):
                if (num >= 1):
                    if row_nums[num-1] in rules_dict[row_nums[num]]:
                        is_sorted = False
                        break
            if is_sorted:
                sorted_pages.append(row_nums)
        
        mid_page_number_sum = 0
        for pages in sorted_pages:
            mid = len(pages) // 2
            mid_page_number_sum += pages[mid]

        return mid_page_number_sum

s = Solution()
res = s.check_page_ordering(text)
print(res)
