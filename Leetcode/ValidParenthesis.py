# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#DIFFICULTY LEVEL: EASY 

from  pythonds.basic import stack

class Solution(object):

    def isValid(self, s):
        """_summary_

        Args:
            s (_type_): _description_
        """
        #initialize 
        
        balanced = True
        data_structure = stack()
        index = 0
        
        #pseudocode:
         
        
        while index < len(s) and balanced:
           valid_string = s[index]
           if valid_string in "([{":
               return data_structure.push(s)
           else:
               if not match( open = "something", close = valid_string) and balanced:
                   return False
            
        index = index + 1
           
    
           
        if s.isEmpty() and balanced:
            return True      
        

def match(open, close):
    open_char = "([{"
    close_char = "}])"
    # checker for matching character 
    return open_char.index(open) == close_char.index(close_char)