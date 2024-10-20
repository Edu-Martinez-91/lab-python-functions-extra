def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here

    set_1=set(lst)

    lst=list(set_1)

    return lst

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    
    """
    string_upp=[]
    string_low=[]
    for i in string:
        if i.isupper()==True:
            string_upp.append(i)
        elif i.islower()==True:
            string_low.append(i)
    return f"Uppercase count: {len(string_upp)}, Lowercase count: {len(string_low)}, tuple: {(len(string_upp),len(string_low))}."

def remove_punctuation_f(sentence):
    import string
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    sentence_new=sentence.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ")
    
    return sentence_new

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here
    translator = str.maketrans('', '', string.punctuation) ## maketrans aquí tiene un tercer argumento (ya que tiene dos comas) que es donde se eliminará lo que aparezca (punctuation)
    new_sentence = sentence.translate(translator).split()  ## La función translate modifica el input (sentence) mediante el argumento (translator) ya sin puntuación (y sin espacios adicionales por eliminación de caracteres de puntuación, ya que también desaparecen y solo quedan los espacios en blanco entre palabras.
    return len(new_sentence)

