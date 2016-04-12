def print_only(x):
   y = x * 2
   print y

# let's try to use our 2 functions
print "running print_only ..."
print_only(7)

def print_only(x):
   y = x * 2
   print y

print "running print_only ..."
print_only(7)
# result: running print_only...
#14

def return_only(x):
   y = x * 2
   return y
   
print "running return_only ..."
return_only(7)
#the answer was running return_only...

def print_only(x):
   y = x * 2
   print y

print "printing print_only ..."
print print_only(7)
#the answer was printing print_only
#14
#None

def return_only(x):
   y = x * 2
   return y

print "running return_only ..."
print return_only(7)
#the answer was running return_only...
#14

def print_only(x):
   y = x * 2
   print y

print "using print_only ..."
print_only(7) + 6
#answer: using print_only
#error message
#14
#error message

def return_only(x):
   y = x * 2
   return y

print "using return_only ..."
return_only(7) + 6
#answer : using return_only...
