print('The string is {}'.format("I'm inside it boys"))
#float formating {width:value,precisionf}

print('The string is {0} {0} {0}'.format('amazing','great','okay')) 
print('The string is {a} {c} {b}'.format(a='amazing',b = 'great',c = 'okay'))
#floating point boys   {value:width.precisionf}
#result 
result = 10.213123312
print('The string is {r:1.4f}'.format(r=result))

#another way of using f-strings
name1 = 'lambdababu'
print(f'This is his {name1}')
#easy way to do string interpolation
age = 10
name = 'maya'
print(f'{name} is gonna become {age} this month')