var_a = 1500 + 3000
var_b = 1500 + 3000.00
var_c = "4500"
var_d = 4500.000001
var_e = 1000
var_f = 5000 - 500
var_g = 60000

#print out the following values 
var_a == var_b
print(var_a == var_b) # print true

var_a >= var_b
print(var_a >= var_b) # it print true

var_a > var_b
print(var_a > var_b) # it print false

#var_a > (var_c)
#print(var_a > var_c) # it gives an error because var_a is an integer and var_c is a string


var_a > var_d
print(var_a > var_d) # i can run it and it the result is False as  print

var_g < var_b
print(var_g < var_b) # it print False