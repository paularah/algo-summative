import math


def encrypt(message, key):
    """

    The encrypt function accepts the message to be encyted as a string  in a string and the encyption key 
    as interger key. The text is then encrpted using the key
    Time Complexity -> O(n) where n is the length of the message to  be encrypted. The reason 
    for this is becuase we iterate over the message to be encrypted once throughtout the lifecyle
    of the encyption algorithm.  
    Space Complexity -> O(n) where n is the length of text to be .

    """
    # creates a stack using a python list for keeping track of of the characters in the
    # encrption text
    tracking_stack = []

    # loops through key times
    for index in range(key):

        curr_char_index = index
        # evaluates that while the character at the current
        # index is less than the length of o the text
        while curr_char_index < len(message):
            # pushes the character at the current index to the top of the tracKing_stack
            tracking_stack.append(message[curr_char_index])
            # Increment the  current index the number of key times
            curr_char_index = curr_char_index + key
        # creates the encrpted text by joining all the elements of the tracking stack into a string

    encrypted_text = "".join(tracking_stack)
    return encrypted_text


def decrypt(encrypted_text, key):
    """

    The decrypt function takes in the encrypted text and the key returns the original message 
    Time Complexity O(n) -> where n is the length of encyptedText. This is because we loop over every char in text only once.
    Space Complexity O(n) -> where n is the length of encyptedText.

    """

    # creates an arary of empty elements the size of the length of the encypted text
    encypted_text_array = [""] * len(encrypted_text)

    # computes the length of each key segment
    segment_length = math.ceil(len(encrypted_text) / key)

    # Computes the number of complete sgement by taking the modulo of the length of ebcyrted text and key
    full_segment = len(encrypted_text) % key
    curr_index = 0
    # loos through the key times
    for val in range(key):
        original_char_index = val
        # check if its not a complete segment, subtract 1 from the original segment length
        if full_segment and full_segment <= val:
            num_chars = segment_length - 1
        else:
            num_chars = segment_length

        # For evey key add the  character in the right position in encypted Text Array
        for i in range(num_chars):
            encypted_text_array[original_char_index] = encrypted_text[curr_index]
            curr_index = curr_index + 1
            original_char_index = original_char_index + key
    # recreates the original text by converting all the elements of encrypted text array to a string
    decrypted_text = "".join(encypted_text_array)
    return decrypted_text


print(decrypt(encrypt("Plain text", 2), 2))
print(decrypt(encrypt("Plain text", 3), 3))
