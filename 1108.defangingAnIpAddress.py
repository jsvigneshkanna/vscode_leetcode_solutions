#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Method 1 o(n) space

        # defanged_address = ''
        # for char in address:
        #     if char == '.':
        #         defanged_address += '[.]'
        #     else:
        #         defanged_address += char

        # return defanged_address    

        # Method 2 O(1) space
        return "[.]".join(address.split('.'))
        
# @lc code=end

