
#Donald Trump is a US president
#current US presiden is Donald Trump
a = "Trump"
b = "Donald"
c = "President"
d = "US"
'''
#without format()
print(b,a,'is a',d,c)

#with format function
print("{} {} is a {} {}".format(b,a,d,c))
print("Current {} {} is {} {}".format(d,c,b,a))

#with format function including indexing numbers
print("current {1} {2} {0} {3}".format(a,b,c,d))



#with short form of format()

print(f'{c} of {d} is {b} {a}')

'''
a = 150
b = 'Trump'
c = 50.25
#with % method
print('%d votes got by %s and won by %f'%(a,b,c))















