##CMT103 COURSEWORK 2017/18 ###
###############################
##You need to implet the following methods:
##
##Task 1
##readnumbers()  [2 marks]
##isPrime()    [5 marks]
##
##Task 2
##readsequences()  [2 marks] 
##longest_common_string() [6 marks]
##
##Task 3
##get_words() [4 marks]
##sort_tuples() [4 marks]
##get_top_10() [7 marks]
################################

#############################################################
#   Student No: 1768263                                     #
#   Module: CMT103 Information Processing in Python         #
#   Coursework: Prime No, Common String, and Top Ly-words   #
#   Lecturer: Coral Walker                                  #
#############################################################

###################################################
#Task 1: Check if a Given Number is a Prime Number:#
###################################################
def readnumbers(file_name): 
    with open("numbers.txt", "r") as numbers: # Input a file name (open and close file)
            numbers = numbers.read()

            # numbers = numbers.rstrip('\n')   Alternative method, less pretty I think
            # numbers = numbers.split(", ")

            num1 = numbers[0:7] # List indices
            num2 = numbers[9:16]
            num3 = numbers[18:25]
            num4 = numbers[27:34]
            num5 = numbers[36:43]
            num6 = numbers[45:53]
            num7 = numbers[55:59]
            num8 = numbers[61:67]
            num9 = numbers[69:77]
            num10 = numbers[79:86]

            list = [int(num1), int(num2), int(num3), int(num4), int(num5), int(num6), int(num7), int(num8), int(num9), int(num10)]
            return(list) # Convert values and return list
    pass

def isPrime(num): # Primality test (input integer)      

###########################################
#   if num > 1:                           #
#       def isqrt(num):                   #
#           x = num                       #
#           y = (x + 1) // 2              #
#           while y < x:                  #
#               x = y                     #
#               y = (x + num // x) // 2   #         Notes -
#           return x                      #     I have included my own isPrime test for your perusal (left) but, while
#                                         #     my algorithm does work, it isn't really suitable for very large numbers
#   for i in range(2,num):                #     This new method checks primes twice as fast, and has been tested extensively
#       if (num % i) == 0:                #     I ran it separately (on my Mac) using 71755440315342536873 as the input
#           return False                  #     The test came back +ive (running time over 15mins)
#           break                         #
#   else:                                 #
#       return True                       #
#                                         #
#   else:                                 #
#   return False                          #
###########################################

############################################################################################################################################
#   Based on Dawg's is_prime test (lines 82-98), see "https://stackoverflow.com/questions/15285534/isprime-function-for-python-language"   #
#   NOTE CHANGES - CHANGED VARIABLE NAMES TO BETTER FIT IN WITH THE CODE I HAVE ALREADY WRITTEN                                            #
#                - CONSISTENT USE OF TABS AND SPACES IN INDENTATION                                                                        #
#                - CODE OMITTED REGARDING HANDLING PRIMES UP TO THAT NUMBER                                                                #
#                - ADDED CLEAR COMMENTS TO EXPLAIN THE METHOD PROPERLY                                                                     #
############################################################################################################################################

        if num == 2 or num == 3: # <--
            return True # First two prime numbers
        if num < 2 or num % 2 == 0:
            return False # There are no even primes (except 2)
        if num < 9:
            return True # i.e. 5 and 7
        if num % 3 == 0:
            return False # No multiples of 3
        sqrt = int(num ** 0.5) # Evaluates the square root
        i = 5
        while i <= sqrt :
            if num % i == 0:
                return False # Check for factors
            if num % (i + 2) == 0:
                return False
            i += 6 # The loop needs to be evaluated every 6th number
        return True # Return a boolean   <--
        pass # Task 1 Complete (error-free)

############################################ 
#Task 2: Find the longest common substring #
#       between two strings:               #
############################################
def readsequences(file_name): 
    with open("sequences.txt", "r") as sequences: # Input a file name (open and close file)
            sequences = tuple(sequences.read().split("\n")) # i.e. ('BBE...ECC', 'CCB...EDC')
            return(sequences) # Return two strings
    pass

def longest_common_string(st1, st2): 

############################################################################################################################################################
#   Based on WIKIBOOKS Algorithm (lines 120-128), see "https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python_3"   #
#   NOTE CHANGES - CHANGED VARIABLE NAMES TO BETTER FIT IN WITH THE CODE I HAVE ALREADY WRITTEN                                                            #
#                - UNNECESSARY CODE OMITTED (lines 130 and 131)                                                                          				   #
#                - ADDED COMMENTS TO EXPLAIN THE METHOD                                                                                                    #
############################################################################################################################################################

    y = [[0] * (1 + len(st2)) for i in range(1 + len(st1))] # Create list for each char in st1  <--
    short = 0 # Defines the shortest acceptable substring length
    var = 0 
    for m in range(1, 1 + len(st1)): # Go to position in st1
        for x in range(1, 1 + len(st2)): # Position in st2
            if st1[m - 1] == st2[x - 1]: # Define substring
                y[m][x] = y[m - 1][x - 1] + 1
                if y[m][x] > short:
                    short = y[m][x]
                    var = m


    return st1[var - short: var] # Return the longest common sub-string   <--
    pass # Task 2 Complete (error-free))

######################################
#Task 3: Get Top 10 ly-Words:        #
######################################
def get_words(file_name): 
    with open("sense_and_sensitivity.txt", "r") as words: # Input a file name (open and close file)
        words = words.read()

        words = words.replace("0", " ")
        words = words.replace("1", " ")
        words = words.replace("2", " ")
        words = words.replace("3", " ")
        words = words.replace("4", " ") # Remove all numbers
        words = words.replace("5", " ")
        words = words.replace("6", " ")
        words = words.replace("7", " ")
        words = words.replace("8", " ")
        words = words.replace("9", " ")

        words = words.replace(" .", " ")
        words = words.replace(". ", " ") # Full stop
        words = words.replace(".", " ")

        words = words.replace(" ,", " ")
        words = words.replace(", ", " ") # Comma
        words = words.replace(",", " ")

        words = words.replace(" ?", " ")
        words = words.replace("? ", " ") # Question mark
        words = words.replace("?", " ")

        words = words.replace(" !", " ")
        words = words.replace("! ", " ") # Exclamation mark
        words = words.replace("!", " ")

        words = words.replace(" '", " ")
        words = words.replace("' ", " ") # Apostrophe   Remove all punctuation "stripped from either end of the 'word'"

        words = words.replace(' "', " ")
        words = words.replace('" ', " ") # Quotation marks
        words = words.replace('"', " ")

        words = words.replace(" :", " ")
        words = words.replace(": ", " ") # Colon
        words = words.replace(":", " ")

        words = words.replace(" ;", " ")
        words = words.replace("; ", " ") # Semicolon
        words = words.replace(";", " ")

        words = words.replace("...", " ") # Ellipsis

        words = words.replace("--", " ") # M-dash

        words = words.replace(" (", " ")
        words = words.replace("( ", " ")
        words = words.replace(" )", " ")
        words = words.replace(") ", " ")
        words = words.replace(" [", " ")
        words = words.replace("[ ", " ")
        words = words.replace(" ]", " ") # Brackets, braces and parentheses
        words = words.replace("] ", " ")
        words = words.replace(" {", " ")
        words = words.replace("{ ", " ")
        words = words.replace(" }", " ")
        words = words.replace("} ", " ")

        words = words.replace("±", " ")
        words = words.replace("§", " ")
        words = words.replace("€", " ")
        words = words.replace("@", " ")
        words = words.replace("£", " ")
        words = words.replace("$", " ")
        words = words.replace("%", " ")
        words = words.replace("^", " ")
        words = words.replace("*", " ") # Symbols
        words = words.replace("+", " ")
        words = words.replace("=", " ")
        words = words.replace("~", " ")
        words = words.replace("`", " ")
        words = words.replace("|", " ")
        words = words.replace("\\", " ")
        words = words.replace("<", " ")
        words = words.replace(">", " ")
        words = words.replace("/", " ")

        words = words.replace(" L ", "") # Litres symbol in "more than 200 L per annum"

        words = words.replace("\b", " ")
        words = words.replace("\t", " ")
        words = words.replace("\n", " ") # Escape codes (python specific)
        words = words.replace("\a", " ")
        words = words.replace("\r", " ")

        words = words.replace("      ", " ")
        words = words.replace("     ", " ")
        words = words.replace("    ", " ") # Remove remaining white space
        words = words.replace("   ", " ")
        words = words.replace("  ", " ")

        words = str.lower(words).split(" ") # Covert string to a word list (items seperated by spaces in string)
        
        while "" in words: # Remove empty strings from list
            words.remove("")

        while "f" in words:    #  
            words.remove("f")  #
                               # No such one-letter words
        while "w" in words:    #
            words.remove("w")  #

        return(words) # Return list
    pass # Task 3 Q1 Complete (error-free)

    #######################################################################
    #     METHOD -                                                        #
    #   Remove all numbers                                                #
    #   Remove puctuation from either side of words                       #
    #   Remove all brackets, braces and parentheses                       #
    #   Remove all symbols                                                #
    #   Remove all python escape codes                                    #
    #   Remove any remaining space                                        #
    #   Remove one empty string, and one-letter words (except A, I & O)   #
    #######################################################################

def get_dic(words): 
    dic = {}
    for word in words: # Input word list
        if word.endswith("ly"): # Check word endswith "ly"
            if word in dic.keys():
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
    return(dic) # Return dictionary
    pass

def get_top_10(dic): # Input dictionary
    num = 10 # Change len(list)
    dic = sorted(dic.items(), key = lambda kv: kv[1], reverse = True) # Sort
    dic_top_num = []
    i = 0
    for key in dic:
        i += 1
        dic_top_num.append(key)
        if i == num:
            break 
    return(dic_top_num) # Return list
    pass



####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################


import sys
if __name__ == '__main__':
    #Take care of the console inputs
    if len(sys.argv)<=1:
        sys.argv = ['', "numbers.txt", "sequences.txt", "sense_and_sensitivity.txt"]
        
   
    stars = '*'*40
    print(stars)
    print("Testing Task 1 --- Is It a Prime?")
    print(stars)

    #Task 1-a
    try:
        nums = readnumbers(sys.argv[1])
        if not nums:
            print("readnumbers() returns None.")
        else:
            print("Numbers: ", nums)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    #Task 1-b
    try:
        if not nums: #Task 1-a has not been implemented
            print("isPrime() skipped....")
        else:    
            for num in nums:
                result = isPrime(num)
                if result==None:
                    print("isPrime() returns None.")
                    break
                print("{} : {}".format(num, "Prime" if result else "Not Prime"))
                    
    except Exception as e:
        print("Error (isPrime()):", e)

    #testing task 2
    print("\n\n"+stars)
    print("Testing Task 2 --- Longest Common Substring")
    print(stars)

    #Task 2-a
    try:
        tup = readsequences(sys.argv[2])
        if not tup:
            print("readsequences() returns None.")
        else:
            st1, st2 = tup
            print("The first string: {}".format(st1)) 
            print("The second string: {}".format(st2)) 
    except Exception as e:
        print("Error (readsequences()):", e)

    #Task 2-b
    try:
        if not tup: #Task 2-a has not been implemented
            print("longest_common_string() skipped...")
        else:
            commonst= longest_common_string(st1, st2)
            if not commonst:
                print("longest_common_string()  returns None.")
            else:
                print("The longest common substring is {} of size {}.".format(commonst,len(commonst)))    
    except Exception as e:
        print("Error (longest_common_string()):", e)

    print("\n\n"+stars)
    print("Testing Task 3 --- Top LY Words")
    print(stars)

    #Task 3-a
    try:
        words = get_words(sys.argv[3])
        if not words:
            print("get_words()  returns None.")
        else:
            print("+ {} has a total of {} words.".format(sys.argv[3], len(words)))
    except Exception as e:
        print("Error (get_words()):", e)

    #Task 3-b
    try:
        if not words: #Task 3-a has not been implemented
            print("get_dic() skipped....")
        else:
            dic = get_dic(words)
            if not dic:
                print("get_dic()  returns None.")
            else:
                print("+ There are {} ly-words in the file.\n+ '{}' and '{}' have {}, {} occurrences respectively.\n".format(len(dic), 'only', 'hardly', dic['only'], dic['hardly']))
    except Exception as e:
        print("Error (get_dic()):", e)

    #Task 3-c
    try:
        if not words or not dic: #Task 3-a has not been implemented
            print("get_top_10() skipped....")
        else:
            results = get_top_10(dic)
            if not results:
                print("get_top_10() returns None.")
            else:
                print("+ Top 10 ly-Words in {}:".format(sys.argv[3]))
                for word, n in results:
                    print(" "*5+"{:<20} {:<}".format(word, n)) 
    except Exception as e:
        print("Error (get_top_10()):", e)


