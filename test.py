# input = int(input('Enter a credit card Number:'))
# input=str(input)
# if len(input) == 8:
#     val = int(len(input)/2)
#     input2 = '*'*val+input[-4:]
#     print(input2)
# else:
#     print('Try Again!!!')


# def myfunc(x):
#     new_lst = []
#     for i in lst:
#         if type(i) == int:
#             if i > 0:
#                 new_lst.append(i)
#     return new_lst
# lst = [1,2,3,'a','b','#',-1,-2]
# # lst = myfunc(lst)
# # print(lst)
# lst = [ i for i in lst if type(i) == int and i >0]
# print(lst)
# def myfunc(x):
#     new_lst = []
#     for i in lst:
#         if str(i).isdigit():
#             if i > 0:
#                 new_lst.append(i)
#     return new_lst
# lst = [1,2,3,'a','b','#',-1,-2]
# lst = myfunc(lst)
# print(lst)

# x = "now"
# val=''
# times=5
# for i in x:
#     val += i*times
# print(val)

# x = 8
# lst =[i for i in range(1,x+1) if x%i == 0]
# # for i in range(1,x+1):
# #     if x % i == 0:
# #         lst.append(i)
# print(lst)


# dict1 = {'a':10,'b':20,'c':30}
# dict2 = {'a1':100,'b1':200,'c1':300}

# dict3 = {**dict1,**dict2}
# print(dict3)

# lst = [1,2,3,4,5]
# new_lst = []
# for i in range(len(lst)-1,-1,-1):
#     new_lst.append(lst[i])
# print(new_lst)

# lst = [1,2,3,4,5,6,7,8,9,10,10]
# lst.sort()
# lst = lst[-1]
# lst = max(lst)
# temp = lst[0]
# for i in lst:
#     if i> temp:
#         temp = i
# print(temp)
# s = 2
# e = 5
# lst = lst[s:e]
# print(lst)
# lst.reverse()
# # lst.reverse()
# print(lst)
# flag = False
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] == lst[j]:
#             flag = True
#             print(True)
#             break
#     if flag:
#         break
# else:
#     print(False)

# dict_temp = {'a':10,'b':20,'c':30,'a':10,'b':20,'c':30,'a':20}
# dict_temp2 = {}
# temp = []
# for i,j in dict_temp.items():
#     if j not in temp:
#         temp.append(j)
#         dict_temp2[i] = j
# print(dict_temp2)

# to find check whether the string is palidrome or not
# input1 = 'abas'
# val = input1
# temp = ''
# for i in input1:
#     for j in range(len(i)):
#         for k in i[j]:
#             temp+=k
# print(val, temp)
# if temp == val:
#     print('palidrome')
# else:
#     print('not palidrome')

# def palindrome_symmetrical(x):

#     #palindrome_1
#     # val = x[::-1]
#     # return True if val == x else False

#     #palindrome_2
#     # mid = (len(x)-1)//2
#     # s = 0
#     # last = len(x) -1
#     # flag = 0

#     # while(s <= mid):
#     #     if x[s] == x[last]:
#     #         s+=1
#     #         last-=1
#     #     else:
#     #         flag = 1
#     #         break
#     # if flag == 0:
#     #     return True
#     # else:
#     #     return False

#     #symmetrical
#     if x[:len(x)//2]== x[len(x)//2:]:
#         return True
#     else:
#         return False
# string = 'abcabc'
# val = palindrome_symmetrical(string)
# if val:
#     print('yes')
# else:
#     print('no')


# import time
# start_time = time.time()
# a = 50
# temp = 1
# while(a>0):
#     temp*=a
#     a-=1
# print(temp)
# end_time = time.time()
# execution_time = end_time-start_time
# print(execution_time)


# start_time1 = time.time()
# b=50
# res = 1
# for i in range(1,b+1):
#     res*=i
# print(res)
# end_time1 = time.time()
# execution_time1 = end_time1-start_time1
# print(execution_time1)


# lst = ['cat','mouse','python','developer']
# val = lst.clear()
# print(lst,val)
# # max_length = max(len(i) for i in lst)
# # print(max_length)
# max_str = [i for i in lst if max(len(i) for i in lst) == len(i)]
# print(max_str)

# print(max(lst,key=len))

# lst = ['ab','aabb','aabbcc','aabbccdd']
# print(max(lst,key=lambda x: len(set(x))))


# a,b = 112,51
# temp = a if a>b else b


# if int(temp) % 2 ==0:
#     print(temp)
# else:
#     temp-=1
#     print(temp)

# def myfunct(x):
#     final_result = []
#     mylist =[]*len(x)

#     val= ['.txt','.exe','.dll']
#     mylist = list(map(lambda x:x.replace('.',''),val))
#     for i in x:
#         pre= i.split('.')[0]
#         suff= i.split('.')[1]

#         if suff in mylist and (len(pre) < 4):
#             final_result.append(True) 
#         else:
#             final_result.append(False) 
#     return final_result

# lst = ['abc.txt','windows.dll','temp.jpg', 'test.py','win32.exe','val.exe']
# print(myfunct(lst))

# x= 5
# mylist =[None]*x
# print(mylist)

# import calendar
# year = int(input('Enter Year :'))
# month_num = int(input('Enter Month :'))
# print(calendar.month(year,month_num))

# from calendar import *
# year = int(input('Enter year :'))
# print(month(year,2))

# string = "HeLLo"
# lst=[]
# for i in range(len(string)):
#     if string[i].isupper():
#         lst.append(i)
# print(lst)

# def func(x):
#     if len(x) % 2 != 0:
#         return x[int((len(x)/2))]
#     else:
#         return None
# string = "abcdefghi"
# print(func(string))


# a = {"a" : "online",
#      "b" : "online",
#      "c" : "offline"
#      }
# count=0
# for i in a.values():
#     if i.values() == 'online':
#         count+=1
#     else:
#         pass
# print(count)

# def func(x):
#     # for i,j in zip(x,x[1:]):
#     #         if i == j:
#     #             return True
#     # return False

#     for i in range(len(x) - 1):
#         if x[i]==x[i+1]:
#             return True
#     return False

# string = "heLlo"
# print(func(string))

# def func(x):
#     temp = ''
#     for i in range(len(x)):
#         if i == len(x)-1:
#             temp += x[i]
#         else:
#             temp+=x[i]+'.'
#     return temp

# string = "test"
# print(func(string))

# s = "t.e.s.t"
# val = list(s)
# result = '.'.join(val).replace('.','')
# print(val,result)

# s = "ter-min-a-tor"
# result = s.split('-')
# print(len(result))

# val = 1000000
# print(f"{val:,}")

# def fuct(*args):
#     return len(args)

# # print(fuct(2,3,4))

# def zap(a,b):
#     # return list(zip(a,b))
#     lst=[]
#     for i in range(len(a)):
#         lst.append((a[i],b[i]))
#     return lst
# print(zap([0,1,2,3],[5,6,7,8]))


# a={'a':10,'b':20,'c':30}
# b={'a1':100,'b1':200,'c1':300}
# print({**a,**b})


# a = str(153)
# res=0
# for i in range(len(a)):
#     res += (int(a[i])**3)
# if int(a)==res:
#     print("Yes")
# else:
#     print("No")

# lst = []
# for i in range(1,1540):
#     length = len(str(i))
#     temp = i
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit**length
#         temp //= 10
#     if i == sum:
#         lst.append(sum)
# print(lst)


# class string: 
      
#     def __init__(self, string): 
#         self.string = string  
          
#     def __repr__(self): 
#         return 'Object: {}'.format(self.string) 
          
#     def __add__(self, other): 
#         return self.string + other 

# string1 = string('Hello') 
    
# print(string1 +' Geeks') 

# lst = [7,2,1,4,3,6,5]
# print(lst.count(5))

# import random
# print(random.randint(0,1))
# print(random.randrange(0,2))

# text = "Hello World"
# import time
# for i in range(len(text)):
#     sub = text[:i+1]
#     for j in range(97,123):
#         print(sub+" "+ chr(j))
#     time.sleep(1)
# string = "aba"
# print("Palindrome" if string == string[::-1] else "Not")

# fact = lambda n:1 if n==0 else n*fact(n-1)
# print(fact(5))

# lst = [9,8,7,5,4,3,1,0]
# lst = sorted(lst)
# print(lst)
# print(sorted(set(lst))[1])

# for i in range(2):
#     for j in range(2-i):
#         print('&',end='')
#     for j in range(i):
#         print('*',end='')
#     print()


# l=5
# k=0
# for i in range(5,0,-1):
#     for j in range(k,l):
#         print(' ',j+1,end='')
#     k+=1
#     print("\t")

# for i in range(97,101):
#     for j in range(97,i):
#         print(" ",end="")
#     for k in range(i,101):
#         print(chr(k)," ",end="")
#     print()

# sub = 'Python'
# val = "Best"

# print(f"{sub} is {val}")
# print("{} is {}".format(sub,val))

# print("{0} is {1} is {1} is {1} is {1} an {1}".format(sub,val))

# pi=3.123456789
# print(f"the value of pi is {pi:.2f}")

# lst = [10,20,30,20]

# for i in lst:
#     val = lst.count(i)
#     if val >1:
#         print(i)
#         break

# from  collections import Counter
# lst = [10,20,30,20]
# print(Counter(lst))

# lst = [10,20,30,20,30]
# val = list(set([x for x in lst if lst.count(x) > 1]))
# print(val)

# string = 'abcabcabc'
# print(''.join(sorted(set(string))))

# temp = [("akash",10),("gaurav",12),("anand",14)]
# print(dict(temp))

# letters=['a','r','s','e','x','p','o']
# vowels=['a','e','i','o','u']

# filters_items = lambda x : False if x in vowels else True

# print(list(filter(filters_items,letters)))

# lst = [1,2,3,4,5]
# val = list(filter(lambda x:x>2,lst))
# print(val)


# for i in range(1,6):
#     x='* '
#     x*=i
#     print(f'{x:^10}')

# for i in range(5,0,-1):
#     x='* '
#     x*=i
#     print(f'{x:^10}')

# m={'a':10,'b':210}
# print(max(m,key=m.get('')))
# print(max(m.keys()))

# # print(m['c'])
# print(m.get('c'))

# lst=['aa','ab','ac','ad']
# print(lst[1:][:2])

# class student:
#     def __init__(self,id_):
#         self.id_ = id_
# obj = student(100)
# obj.__dict__['name'] = 'John'
# print(obj.__dict__)
# print(obj.id_+len(obj.__dict__))


# def funct(x,y):
#     return x if y>0 else y
# result = funct(5,0)+funct(0,-5)
# print(result)

# lst=[True,False,False]
# x=any(lst)
# print(x)

# t=(False,0,0)
# for i in t:
#     print(i)
# print(t)
# y=any(t)
# print(y)

# l1=[1,2.3]
# l2=[4]
# print(list(zip(l1,l2)))

# e = enumerate(['a','b'],5)
# for i ,c in e:
#     print(i,c,end=' ')

from datetime import datetime,timedelta

start_date = datetime.today().date()
deadline_date = (datetime.today() + timedelta(days=30)).date()
diff = (deadline_date- start_date).days
print(start_date,deadline_date,diff)
print(type(start_date),type(deadline_date),type(diff))
