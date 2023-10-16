
def is_correct_string(strx):
    strx = strx.lstrip()
    if strx[0] == "+" or strx[0] == "-":
        strx = strx[1:]
    strx += " "
    math_sign = ["+", "-", "*", "/"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arr_check = []
    curr_str = ""
    for i in strx:
        if i in math_sign or i == " ":
            if len(curr_str) != 0:
                if curr_str[-1] == ".":
                    return False
                else:
                    arr_check.append(curr_str)
                    curr_str = ""
            if i != " ":
                arr_check.append(i)
        elif i == ".":
            if len(curr_str) == 0:
                return False
            elif "." in curr_str:
                return False
            else:
                curr_str += i
        elif i in numbers:
            curr_str += i
        else:
            return False

    if (arr_check[0] in math_sign and (arr_check[0] != "-" or arr_check[0] != "+")) or (arr_check[-1] in math_sign):
        return False
    else:
        curr_state = ""
        if arr_check[0] in math_sign:
            curr_state = "SIGN"
        else:
            curr_state = "NUMBER"
        last_sign = ""
        for i in arr_check[1:]:
            if i in math_sign:
                if curr_state == "SIGN":
                    return False
                else:
                    last_sign = i
                    curr_state = "SIGN"
            else:
                if curr_state == "NUMBER":
                    return False
                else:
                    if last_sign == "/" and i == "0":
                        return False
                    else:
                        curr_state = "NUMBER"
        return True


if __name__ == '__main__':
    string = input()
    while string != "end":
        if is_correct_string(string):
            try:
                print(eval(string))
            except Exception as e:
                print("EVAL ERROR!")
        else:
            print("Incorrect expression")
        string = input()
