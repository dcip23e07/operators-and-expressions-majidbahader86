
# (5 > 4) and (3 == 5) 
# not (5 > 4) 
# (5 > 4) or (3 == 5) 
# not ((5 > 4) or (3 == 5)) 
# (True and True) and (True == False) 
# (not False) or (not True)

(5 > 4) and (3 == 5) 
5 > 4 is True
3 == 5 is False
# the expression is false

not (5 > 4) 
5 > 4 is True
# not declares the value, so the expression becomes false 

(5 > 4) or (3 == 5) 
5 > 4 is True
3 == 5 is False 
# or operator returns true, if at least one of the operands is True
# therefore the expression is true

not ((5 > 4) or (3 == 5)) 
5 > 4 is True 
3 == 5 is False 
# or operator returns true, if at least one of the operands is True
# but not negates the value, the expression is false 

(True and True) and (True == False) 

True and True is True
True == False is False 
# the and operator returns True if both operands are true 
# the expression evaluates False 

(not False) or (not True)
not False is True
not True is False 
# the or operator returns True if atleast one of the operands is true 
# therefore, this expression evaluates to true 