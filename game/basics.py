"""
# Put all imports into the functions, top level imports and variables break the game server

# Example function:
def example(data = None, answer = None, **kwargs):
    '''Doc strings show'''
    # Check to see if the user is requesting data or submitting an answer
    if answer == None:
        # Return the data you want the user to work against, any format
        # Random data can be passed here, it is cached prior to use
        return data
    else:
        # Compare submitted answer to expected answer
        # data is what was originally given to the user, answer is what they are claiming to be the answer
        return answer == data
"""
# Any global variable will be exposed to the game engine as an available challenge to solve
# Unless you preface it with a single or double underscore
_lorem = "Lorem ipsum dolor sit amet consectetur adipiscing elit Proin quam mi hendrerit vehicula convallis ac egestas et erat Etiam eget enim ligula Nulla sed pellentesque nunc Vivamus mollis sapien sapien id malesuada ligula ullamcorper dictum Proin tortor lacus suscipit suscipit justo a maximus finibus massa Nam id facilisis odio Morbi eu egestas lacus nec varius ante Etiam non ultricies ipsum Duis ut orci elit Aliquam dictum metus congue molestie neque a pretium enim Maecenas vitae ipsum et sapien imperdiet lacinia sed quis turpis"

# kwargs is a catch all for future compatability, right now it only contains "playerName"
def A_str_to_int(data = None, answer = None, **kwargs):
    '''Given a string, return an integer'''
    from random import randint
    if answer == None:
        return str(randint(100, 999))
    else:
        return answer == int(data)

def B_int_to_str(data = None, answer = None, **kwargs):
    '''Given an integer, return a string'''
    from random import randint
    if answer == None:
        return randint(100, 999)
    else:
        return answer == str(data)

def C_str_to_list(data = None, answer = None, **kwargs):
    '''Given a sentence of words, return a list splitting on underscores'''
    from random import choice, randint
    if answer == None:
        data = []
        for i in range(randint(5, 8)):
            data.append(choice(_lorem.split(" ")))
        return "_".join(data)
    else:
        return answer == data.split("_")

def D_sum_from_list(data = None, answer = None, **kwargs):
    '''Given a list of numbers as strings, return a sum of all items'''
    from random import randint
    if answer == None:
        return map(str, [randint(1, 20) for x in range(randint(3, 5))])
    else:
        return answer == sum(map(int, data))

def E_merge_list(data = None, answer = None, **kwargs):
    '''Given a list of words, return a single string containing all the words deliminated by a space'''
    from random import choice, randint
    if answer == None:
        data = []
        for i in range(randint(3, 5)):
            data.append(choice(_lorem.split(" ")))
        return data
    else:
        return answer == " ".join(data)

def F_filter_list(data = None, answer = None, **kwargs):
    '''Given a list of numbers, return a list only containing the even elements'''
    from random import randint
    if answer == None:
        return [randint(5, 20) for x in range(randint(15, 20))]
    else:
        return answer == filter(lambda x: x % 2 == 0, data)

def G_slice_str(data = None, answer = None, **kwargs):
    '''Given a tuple containing a string(0) and a number(1), return the X first characters of the string where X is the number'''
    from random import choice, randint
    if answer == None:
        data = []
        for i in range(10, 15):
            data.append(choice(_lorem.split(" ")))
        return (" ".join(data), randint(10, 20))
    else:
        return answer == data[0][:data[1]]

def H_reverse_str(data = None, answer = None, **kwargs):
    '''Given a string, return the reverse of that string'''
    from random import choice, randint
    if answer == None:
        data = []
        for i in range(randint(3, 5)):
            data.append(choice(_lorem.split(" ")))
        return " ".join(data)
    else:
        return answer == data[::-1]

def I_key_value(data = None, answer = None, **kwargs):
    '''Given a tuple containing a dictionary(0) and a key(1), return the value stored at the key'''
    from random import choice, randint
    if answer == None:
        data = {choice(_lorem.split(" ")): choice(_lorem.split(" ")) for i in range(randint(15, 20))}
        return (data, choice(data.keys()))
    else:
        return answer == data[0][data[1]]
