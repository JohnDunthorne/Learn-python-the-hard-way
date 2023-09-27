types_of_people = 10
2 x = f"There are {types_of_people} types of people."
3
4 binary = "binary"
5 do_not = "don't"
6 y = f"Those who know {binary} and those who {do_not}."
7
8 print(x)
9 print(y)
10
11 print(f"I said: {x}")
12 print(f"I also said: '{y}'")
13
14 hilarious = False
STRINGS AND TEXT 53
15 joke_evaluation = "Isn't that joke so funny?! {}"
16
17 print(joke_evaluation.format(hilarious))
18
19 w = "This is the left side of..."
20 e = "a string with a right side."
21
22 print(w + e)