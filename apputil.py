

# add code below ...


#EXERCISE 1

#-----IMPORTS-----#
import re

#-----FUNCTION DEFS-----#
def palindrome_detector(user_input):

    #debugging code
    print("User entered the following text: " + user_input)
    print("Length of user entered text is: ", len(user_input))

    #set pointer positions
    #set at starting index of array
    left_pointer = 0
    #set at the end index of array
    right_pointer = len(user_input) - 1

    

    #compare characters at each end cycling inwards
    while left_pointer < right_pointer:
        if user_input[left_pointer] != user_input[right_pointer]:
            print("This text is NOT a palindrome")
            return False
        left_pointer += 1
        right_pointer -= 1

    print("This text IS a palindrome")
    return True
#-----------------------#




#-----MAIN-----#
user_input = input("Enter a string to be tested: ")
user_input = user_input.lower()


#puncuation is removed and replaced by the empty string
user_input = re.sub(r'[^\w\s]', '', user_input)

#spaces are replaceed with the empty string
user_input = re.sub(r'\s', '', user_input)

#call function
palindrome_detector(user_input)



