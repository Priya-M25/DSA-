class Solution:
     def reverseWord(self, str: str) -> str:
        return str[::-1]
        
if __name__ == "__main__":
    t = int(input("enter :"))
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

#--------------------------------
#2nd solution
class Solution:
     def reverseWord(self, str: str) -> str:
        r=""
        for i in range(len(str)-1,-1,-1):
            r+=str[i]
        return r
if __name__ == "__main__":
    t = int(input("enter :"))
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1
