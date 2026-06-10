class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mp={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1]!=mp[i]:
                    return False
                stack.pop()
 
                
        if len(stack)==0:
            return True
        else:
            return False
        
                    