class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j=len(a)-1, len(b)-1 
        tot,carry='',0
        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            s = x + y + carry
            tot += str(s % 2)
            carry = s // 2
            i -= 1
            j -= 1
        return tot[::-1]