def arithmetic_arranger(problems, show_answers=False):

#1 check the length of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    oprt=[]    
#2 check the operator
    for pb in problems:
        arry = pb.split()
        oprt.append(arry[1])
    #print(oprt)

    for op in oprt:
        if not op in ["+","-"]:
            return "Error: Operator must be '+' or '-'."

#3 check the non-digit
    numbers=[]
    for pb in problems:
        arry = pb.split()
        numbers.append(arry[0])
        numbers.append(arry[2])

    for nb in numbers:
        if not nb.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(nb)> 4:    
            return 'Error: Numbers cannot be more than four digits.'

#4 design display arithmetic_arranger
    answers=[]
    top_row=''
    bottom_row=''
    dash_row=''
    ans_row=''

    #-start:0
    #-end:len(numbers)
    #-The step value : (increments by 2)   
    for i in range(0,len(numbers),2):
        num1=numbers[i]
        num2=numbers[i+1]
        op=oprt[i // 2]

        if op == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)
        answers.append(result)

        space_width = max(len(num1),len(num2)) + 2
        top_row += numbers[i].rjust(space_width) 
        bottom_row += op+numbers[i+1].rjust(space_width-1) 
        dash_row +='-' * space_width
        ans_row=''

        if i != len(numbers)-2:
            top_row += ' '*4
            bottom_row += ' '*4
            dash_row += ' '*4
    
    #increment by 2 =  2 * i : numbers[2 * i]
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]),len(numbers[2 * i + 1])) + 2
        ans_row += str(answers[i]).rjust(space_width)
        
        
        if i != len(answers)-1:
            ans_row += ' '*4   

    if show_answers:
        arithmetic_arranger = "\n".join((top_row,bottom_row,dash_row,ans_row))
    else:
       arithmetic_arranger = "\n".join((top_row,bottom_row,dash_row)) 
            
    

    return arithmetic_arranger

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')