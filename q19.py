# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class Check:
    # def __init__(self) -> None:
    #     # self.parenthesis = {"(":")","{":"}","[":"]"}
    #     # self.empty = []
    @staticmethod
    def check_par(string):
        length = 0

        while length != len(string):
            length = len(string)
            string = string.replace("()","").replace("{}","").replace("[]","")
        return len(string) == 0   
            

validator = Check()
print(validator.check_par("()"))  # Should return True
print(validator.check_par("()[]{}"))  # Should return True
print(validator.check_par("[)"))  # Should return False
print(validator.check_par("({[)]"))  # Should return False
print(validator.check_par("{{{()}}}"))  



