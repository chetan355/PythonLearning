#format 
num = 12
name = "Chetan"
#print("My number is {one} and name is {two}".format(one=num,two=name))

#string index
s = "hello"
#print(s[0:4])

#list and nested list - list is muttable we can change the elements of list
my_list = [1,3,5]
my_list.append(7)
my_list[0] = 111;
#print(my_list)
#print(my_list[1:2])

nested_list = [1,2,[4,5,['chets']]]
#print(nested_list[2][2][0])

#dictonary - key value pair
d = {'key1':'value1','key2':'value2'}
d['key1'] = [1,2,3]
my_list = d['key1']
#print(my_list[0])
d = {'k1':{'K1':123}}
#print(d['k1']['K1'])

#tuple - immutable (can't change the item of tuple)
t = (1,2,3)
#print(t[0])

#set - collectio of unique elements
my_set = {1,2,1,1,2,2,3,3}
my_set.add(5);
#print(my_set)

#comparision

#print(1>2)
and_check = 1 < 2 and 4 > 3
or_check = 3 < 2 or 4 > 3
#print(or_check)

#if-else block

if 3<2:
    print("True")
elif 3>2:
    print("Woo!")
else:
    print("False")

#for loop 

seq = [1,2,3,4,5]
#for num in seq:
    #print(num)
#for num in range(0,5):
    #print(num)

#list comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2) 
#another way:
out = [num**2 for num in x]
#print(out)


#functions :

def my_func(param1):
    print('Hello '+param1)


def square(num):
    return num**2

op = square(2)
#print(op)

#map and filter , lamda expression

def times2(var):
    return var*2
t = lambda var:var*2

seq = [1,2,3,4,5]
mapped_list = list(map(lambda num:num*3,seq))
#print(mapped_list)

#filter
filtered_list = list(filter(lambda num : num%2 == 0,seq))
#print(filtered_list)

#methods
s = 'hello my name $ is chets'
#string_check = s.lower()
#string_check = s.split();
string_check = s.split('$')
#print(string_check[1])

#tuple in list

x = [(1,2),(2,3),(4,5)]
#print(x[0][1])

#for(a,b) in x:
#    print(b)

#exercise
def domainGet(domain):
    return(domain.split('@')[1])

#print(domainGet('user@domain.com'))

def countDog(var):
    count=0
    list = var.split()
    for x in list:
        if x=='dog':
            count+=1
    return count


#print(countDog('This dog runs faster than the other dog dude!'))

seq = ['soup','dog','salad','cat','great']

my_list = list(filter(lambda str:str[0]!='s',seq))
#print(my_list)
