def summation(*numbers):
    total = 0

    for number in numbers:
        total+= number
            
    return total
    
def obaLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
    
def add_str(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'
        
def sample(word):
    long_word = ""
    max_length = 0
    for sample in word:
        max_length = len(word)
        longest_word = word
    return word
    
def addup(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return string
        
    






