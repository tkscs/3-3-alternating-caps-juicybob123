def alt_caps(original_string):
   
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    string= ""
    x = 1
    y = 0
    new_string = original_string
    for charachter in new_string:
        if y%2 == 0:
            string = charachter.lower()
            print(string)
        if y%2 == 1:
            string = charachter.upper()
            print(string)
        y= y+1
    
    #     (new_string[x:x+1]).upper()
    #     x= x+2
    #     string = string + new_string[x:x+1]
    #     (new_string[y:y+1]).upper()
    #     y = y+2
    #     string = string + new_string
    # print(string)
            
    

    # YOUR CODE HERE
   

    return new_string


print(alt_caps("Alternating Capitalization"))
