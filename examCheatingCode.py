# Compute the honking protocol for the exam cheaters


def compute_and_send_code(exam):
    code = [0] * 10
    # Dont change anything above this line
    # ==========================

    # TODO Add your solution here.
    
    j = 0                                       # Keeping track of j for traversing code[10]
    zero_count = 0                              # Variable for counting 0s
    one_count = 0                               # Variable for counting 1s
    for i in range(20):
        
        if i < 15:                              # Traversing exam[20] till 15 elements.
            if exam[i] == 0:
                zero_count += 1                 # Increasing zeroCount if exam[i] = 0
            else:
                one_count += 1                  # Increasing oneCount if exam[i] = 1
                
            if (i + 1) % 3 == 0:                # Resetting 0s and 1s count if a block of 3 is formed.
                if zero_count > one_count:      # Setting code[j] = 0 if 0s > 1s
                    code[j] = 0
                    j += 1
                    zero_count = 0
                    one_count = 0
                else:
                    code[j] = 1                 # Setting code[j] = 1 if 0s < 1s
                    j += 1
                    zero_count = 0
                    one_count = 0
        else:
            code[j] = exam[i]                   # Setting code[j] same as exam[i] for the last 5 elements.
            j += 1
            zero_count = 0
            one_count = 0
    # ==========================
    # Dont change anything below this line
    return code


def enter_solution_based_on_code(code):
    answer = [0] * 20

    # Dont change anything above this line
    # ==========================

    j = 0                                       # Keeping track of j for traversing answer[20]
    # TODO Add your solution here.
    for i in range(10):
        
        if j < 15:                              # Traversing answer[20] till 15 elements
            if j + 3 > 19:
                break
            
            if code[i] == 0:                    # Expanding 0 to 000 if code[i] = 0
                answer[j] = 0
                answer[j + 1] = 0
                answer[j + 2] = 0
                j += 3
            if code[i] == 1:                    # Expanding 1 to 000 if code[i] = 0
                answer[j] = 1
                answer[j + 1] = 1
                answer[j + 2] = 1
                j += 3
        else:
            answer[j] = code[i]                 # Setting answer[i] as code[i] for the last 5 elements
            j += 1

    # ==========================
    # Dont change anything below this line
    return answer

