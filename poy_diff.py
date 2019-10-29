import re

FILE_NAME= "polylist.in"

list_operators = ['+' , '-']


def zipper(term_list, symbol_list):
    answer = ""
    reduced_list = list(filter(None,term_list))
    if(len(reduced_list)==0):
        answer = "0"
    print(reduced_list)
    #print(len(reduced_list))
    reduced_sym = symbol_list[0:len(reduced_list)-1]
    reduced_sym.append('')
    print(reduced_sym)
    for (t,s) in zip(reduced_list,reduced_sym):
        answer = answer + t + " " + s + " "
    return answer

def seperator(expression):
    constant_part=""
    variable_part=""
    for i in expression:
        if(i>='0' and i<='9'):
            constant_part += i
        else:
            variable_part += i 
    if(constant_part==""):
        int_const = 1
    else:
        int_const = int(constant_part)

    return [int_const,variable_part]

def differentiate_term(source):
    target=""
    temp = re.split('\^',source)
    if(len(temp)==2):
        # Symbol ^ Detected
        #use differentiatiion
        [cons, var] = seperator(temp[0])
        exp = temp[1]
        target =  str(int(exp) * cons) + var + "^" + str(int(exp)-1)
    else:
        #Symbol ^ not present
        #Remove variable and return term
        [cons,var]= seperator(temp[0])
        if(var!=""):
            target = str(cons)
        else:
            target = '0'
    return target

def operand_tokenizer(equation):
    tokenized_list = re.split('\+|-', equation)
    return tokenized_list

def whitespace_remover(sample_string):
    temp=""
    for character in sample_string:
        if(character!=" "):
           temp = temp + character;
    return temp  

def fileReadAndSolve(filename):
    f = open(FILE_NAME, "r")
    answer_list = []
    for line in f:
        result = whitespace_remover(line.split('\n')[0])
        equation = operand_tokenizer(result)
        operator_occurance = []
        for char in result:
            if(char in list_operators):
                operator_occurance.append(char)
        solved_list = []
        for term in equation:
            solved_list.append(differentiate_term(term))
        answer_list.append(zipper(solved_list,operator_occurance))
    return answer_list

answers = fileReadAndSolve(FILE_NAME)
for answer in answers:
    print("Solved value is : " +  answer)
