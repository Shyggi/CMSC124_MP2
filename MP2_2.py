# BNF Grammar
# <pal> ::= aa | bb | cc | ... | zz |
#       ::= AA | BB | CC | ... | ZZ |
#       ::= a<pal>a | b<pal>b | c<pal>c | ... | z<pal>z |
#       ::= A<pal>A | B<pal>B | C<pal>C | ... | Z<pal>Z |
#       ::= <char>
# <char> ::= a | b | c | d | ... | z |
#            A | B | C | D | ... | Z      


import string

class Palindrome:
    def __init__(self, string:str):
        self.unv = string

    def validate_pal(self):
        char_list = string.ascii_letters
        skip = string.whitespace
        for char in self.unv:
            if char not in char_list and char not in skip:
                return False
        clean = (''.join([char for char in self.unv if char in char_list])) 

        l, r = 0, len(clean) - 1

        while l < r:
            if clean[l] != clean[r]:
                return False

            l, r = l + 1, r - 1

        return True

    def palindrome(self):
        print(f"As per BNF, {self.unv} is in the grammar" if self.validate_pal() else f"As per the BNF, {self.unv} is not in the grammar")

def main():
    testcase = input("Enter test case: ")
    Palindrome(testcase).palindrome()


if __name__ == '__main__':
    main()
