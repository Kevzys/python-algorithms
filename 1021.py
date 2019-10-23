def removeOuterParentheses(str):
    open_bracket_count=0
    close_bracket_count=0
    new_list = ""
    final_list = ""
    for x in str:

        new_list += x
        if x == "(":
            open_bracket_count += 1
        else:
            close_bracket_count +=1

        if open_bracket_count == close_bracket_count:
            #made primitive
            #need to remove first and last
            new_list = new_list[1:len(new_list)-1]
            final_list += new_list
            new_list = ""

    return final_list

print(removeOuterParentheses("(()())(())(()(()))"))
