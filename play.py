#!/usr/bin/env python

from game import *

# Create new game object and declare username (for salting purposes)
myGame = engine.handler("Tory")

def main():
    print myGame.help()

    print "Printing help strings for each challenge:"
    challenges = ["A_str_to_int", "B_int_to_str", "C_str_to_list", "D_sum_from_list", "E_merge_list", "F_filter_list", "G_slice_str", "H_reverse_str", "I_key_value"]
    for challenge in challenges:
        print "{}:    \t{}".format(challenge, myGame.help("basics", challenge))

    print "{}:        \t{}".format("net_test", myGame.help("remote", "net_test"))

    # When you submit a challenge, it runs your function 100 times against the solution to check to see if it if always correct.
    # This is to reduce brute force attemps. Print statements are highly discouraged because of this.    
    print myGame.submit("basics", "A_str_to_int", A)
    print myGame.submit("basics", "B_int_to_str", B)
    print myGame.submit("basics", "C_str_to_list", C)
    print myGame.submit("basics", "D_sum_from_list", D)
    print myGame.submit("basics", "E_merge_list", E)
    print myGame.submit("basics", "F_filter_list", F)
    print myGame.submit("basics", "G_slice_str", G)
    print myGame.submit("basics", "H_reverse_str", H)
    print myGame.submit("basics", "I_key_value", I)
    print myGame.submit("remote", "net_test", net_test)

    print "\n" + "#" * 40 + "\n"

    print "Printing scoreboard: (True means a successful completion of the challenge by this player)"
    print myGame.list()

def A(data):
    answer = int(data)
    return answer

def B(data):
    answer = str(data)
    return answer

def C(data):
    answer = data.split("_")
    return answer

def D(data):
    answer = sum(map(int, data))
    return answer

def E(data):
    answer = " ".join(data)
    return answer

def F(data):
    answer = filter(lambda x: x % 2 == 0, data)
    return answer

def G(data):
    answer = data[0][:data[1]]
    return answer

def H(data):
    answer = data[::-1]
    return answer

def I(data):
    answer = data[0][data[1]]
    return answer

def net_test(data):
    answer = sum(data)
    return answer

if __name__ == '__main__':
    main()
