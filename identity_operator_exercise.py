var_a = 400 
var_b = '200' + '200' 
var_c = 400.0 
var_d = 200 + 200

# what is the result of : i. var_a == var_b 
# ii. var_a is var_b 
# (can you explain using comments the reason for the result)


var_a == var_b
var_a # integer
var_b # string 
# == check if the values are equal and it does not perform type checking, so this comparison is True because both var_a and var_b have the same value, which is 400. 

var_a is var_b
var_a # integer
var_b # string object
# is operator checks if the two variables reference the same object in memory.
# This comparison is False because var_a and var_b are different object types

# what is the result of : 
# i. var_a == var_c 
# ii. var_a is var_c (
# can you explain using comments the reason for the result)

var_a == var_c
var_a # integer
var_c # float
# the == operator checks if the values are equal. In this case, it's True because the values are the same.


var_a is var_c 
var_a # integer
var_c # float 
# The is operator checks if the two variables reference the same object in memory.
# This comparison is False because var_a and var_c are different object types 

# what is the result of : 
# i. var_a == var_d 
# ii. var_a is var_d 
# (can you explain using comments the reason for the result)

var_a == var_d
var_a # integer
var_d # integer
# This comparison is True because the values are the same.

var_a is var_d
var_a # integer
var_d # integer
# This comparison is true because var_a and var_d are same object types 