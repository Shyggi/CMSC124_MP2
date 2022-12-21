# BNF Grammar #1
# <expression>  ::= (<expression) | <term> 
# <term>	    ::= <expression> <addoperator> <expression> | ~ <expression> | <identifier>
# <addoperator> ::= + | -
# <identifier>  ::= x | y | z

def countParens(string:str) -> bool:
    counter = 0
    for char in string:
        if char == '(': counter += 1
        if char == ')': counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True

def String(string:str) -> bool:
    identifiers = ['x', 'y', 'z']
    operations = ['+', '-']

    if (countParens(string) == False):
        return False

    for i in range(len(string) - 1):
        current, next = string[i], string[i+1]

        if current in identifiers:
            if next not in operations and next != ')':
                return False
            else:
                continue
        elif current in operations:
            if next not in identifiers and next != '(' and next != '~':
                return False
            else:
                continue
        elif current == '(':
            if next not in identifiers and next != '~' and next != '(':
                return False
            else:
                continue
        elif current == ')':
            if next not in operations and next != ')':
                return False
            else: 
                continue
        elif current == '~':
            if next not in identifiers and next != '(' and next != '~':
                return False
            else:
                continue
        else:
            return False
    return True

def main():
    Case = input("\nEnter test case: ")
    print(f"{Case} is in the grammar" if String(Case) else f"{Case} is not in the grammar")

if __name__ == '__main__':
    main()
