##PROBLEM1:

#say hello world with python
#print('Hello, world!')

#python if else
# import math
# import os
# import random
# import re
# import sys
# if __name__ == '__main__':
#     n = int(input().strip())

# if (n % 2 != 0 and 1 <= n < 100) or (n % 2 == 0 and 6 <= n <= 20):
#     print('Weird')
# else:
#     (n % 2 == 0 and 2 < n < 5 or 20 < n <= 100)
#     print('Not Weird')

#arithmetic operators
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())

#     print(a+b)
#     print(a-b)
#     print(a*b)

#python division
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(int(a/b))
#     print(a/b)

#loops
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0,n):
#         print(i**2)

#write a Function
# def is_leap(year):
#     if year%400== 0:
#         return True
#     if year%100==0:
#         return False
#     if year%4==0:
#         return True
#     else:
#         return False
# year = int(input())
# print(is_leap(year))

#print function
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i, end="")

#list comprehnsion
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
# lists= [[i, j , k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!= n]
# print(lists)

#find the runner up score
# n = int(input())
# arr= map(int, input().split())
# scores=set(list(arr))
# scores.remove(max(scores))
# print(max(scores))

#nested list
# if __name__ == '__main__':
#     l= []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name,score])
# sorted_grades= sorted(list(set([x[1] for x in l])))
# second_lowest= sorted_grades[1]
# low_f_l= []
# for student in l:
#     if second_lowest == student[1]:
#         low_f_l.append(student[0])
# for student in sorted(low_f_l):
#     print(student)

#finding the percentage
# n= int(input())
# student_marks= {}
# for _ in range(n):
#     name, *line= input().split()
#     scores= list(map(float, line))
#     student_marks[name]= scores
# query_name= input()
# scoreList= sum(student_marks[query_name])
# average= scoreList/len(student_marks[query_name])
# print('%.2f'%average)

#Lists
# list= []
# N= int(input())
# for s in range(0, N):
#     cmd= input(). split()
#     if cmd[0]== 'insert':
#         list.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0]== 'print':
#         print(list)
#     elif cmd[0]== 'remove':
#         list.remove(int(cmd[1]))
#     elif cmd[0]== 'append':
#         list.append(int(cmd[1]))
#     elif cmd[0]== 'sort':
#         list.sort()
#     elif cmd[0]== 'pop':
#         list.pop()
#     else:
#         list.reverse()

#tupels
# n = int(input())
# t=tuple(map(int, input().split()))
# print(hash(t))

#swap case
# def swap_case(s):
#     string= ''
#     for i in s:
#         if (i.isupper()== True):
#             string += i.lower()
#         elif (i.islower()== True):
#             string += i.upper()
#         else:
#             string += i
#     return string

#string,split and join
# def split_and_join(line):
#     a= line.split(" ")
#     b= "-".join(a)
#     return b
# line = input()
# result = split_and_join(line)
# print(result)

#whats your name
# def print_full_name(first, last):
#     print(f'Hello {first} {last}! You just delved into python.')
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

#mutations
# def mutate_string(string, position, character):
#     return string[:position]+ character + string[position+1:]
# s = input()
# i, c = input().split()
# s_new = mutate_string(s, int(i), c)
# print(s_new)

#find a string
# def count_substring(string, sub_string):
#     i=0
#     for sub in range(len(string)- len(sub_string)+1):
#         if string[sub:sub+len(sub_string)]== sub_string:
#                 i+=1
#     return i
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)

#string validators
# s=input()
# print(any(map(str.isalnum,s)))
# print(any(map(str.isalpha,s)))
# print(any(map(str.isdigit,s)))
# print(any(map(str.islower,s)))
# print(any(map(str.isupper,s)))

#text alignment
# thickness = int(input()) #This must be an odd number
# c = 'H'

# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))

# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#text wrap
# import textwrap
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

#designer door mat
# n, m= map(int,input().split())
# for i in range(1,n,2):
#     print(('.|.' *i).center(m, '-'))
# #welcome
# print('WELCOME'.center(m, '-'))
# for i in range(n-2,-1,-2):
#     print(('.|.' *i).center(m, '-'))

#string formating
# def print_formatted(number):
#     lenght= len(bin(number)[2:])
#     for i in range(1,number+1):
#         print(str(i).rjust(lenght,' '),end=" ")
#         print(oct(i)[2:].rjust(lenght,' '),end=" ")
#         print(((hex(i)[2:]).upper()).rjust(lenght,' '),end=" ")
#         print(bin(i)[2:].rjust(lenght,' '),end=" ")
#         print("")

#Alphabet rangoli
# def print_rangoli(size):
#     w= size*4-3
#     string= ''
#     for i in range(1,size+1):
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < w :
#                 string += '-'
#         for k in range(i-1,0,-1):
#             string += chr(97+size-k)
#             if len(string) < w :
#                 string += '-'
#         print(string.center(w,'-'))
#         string = ''
#     for i in range(size-1,0,-1):
#         string = ''
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < w:
#                 string += '-'
#         for k in range(i-1,0,-1):
#             string += chr(97+size-k)
#             if len(string) < w:
#                 string += '-'
#         print(string.center(w,'-'))

#Capitalize
# def solve(s):
#     for i in s.split():
#         s = s.replace(i,i.capitalize())
#     return s

#the minion game
# def minion_game(string):
#     score1=0 #Kevin,v
#     score2=0 #Stuart,c
#     for i in range(len(string)):
#         if string[i] in 'AEIUO':
#             score1+= len(string)-i
#         else:
#             score2+= len(string)-i
#     if score1>score2:
#         print('Kevin', score1)
#     elif score1<score2:
#         print('Stuart', score2)
#     elif score1==score2:
#         print('Draw')
#     else:
#         print('Draw')

#merge the tools
# def merge_the_tools(string, k):
#     a= int(len(string) / k)
#     for i in range(a):
#         t = string[i * k : (i+ 1) * k]

#         u = ""
#         for s in t:
#             if s not in u:
#                 u += s
#         print(u)

#Introduction to sets
# def average(array):
#     ave= (sum(set(arr))/len(set(arr)))
#     ave= round(ave, 3)
#     return ave
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

#no idea
# n_m= map(int,input().split())
# n= list(map(int,input().split()))
# mA= set(map(int,input().split()))
# mB= set(map(int,input().split()))
# print(sum([(i in mA)- (i in mB) for i in n]))

#set.add()
# n= int(input())
# set=set()
# for i in range(n):
#     name=input()
#     set.add(name)
# a= len(set)
# print(a)

#Set .discard(), .remove() & .pop()
# n= int(input())
# s= set(map(int,input().split()))
# N= int(input())
# for i in range(N):
#     cmd=input().split()
#     if cmd[0]== 'pop':
#         s.pop()
#     elif cmd[0]== 'remove':
#         s.remove(int(cmd[1]))
#     elif cmd[0]== 'discard':
#         s.discard(int(cmd[1]))
# print(sum(s))

#Symmetric difference
# m= int(input())
# a= set(map(int, input().split()))
# n= int(input())
# b= set(map(int, input().split()))
# c1=a.union(b)
# c2= a.intersection(b)
# c3= list(c1.difference(c2))
# c3.sort()
# for i in c3:
#     print(i)

#set.union opration
# n= int(input())
# nE= set(map(int, input().split()))
# b= int(input())
# bF= set(map(int, input().split()))
# c= list(nE.union(bF))
# print(len(c))

#set.intersection opration
# n= int(input())
# nE= set(map(int, input().split()))
# b= int(input())
# bF= set(map(int, input().split()))
# c= list(nE.intersection(bF))
# print(len(c))

#Set difference opration
# n= int(input())
# nE= set(map(int, input().split()))
# b= int(input())
# bF= set(map(int, input().split()))
# c= nE - nE.intersection(bF)
# print(len(c))

#set.symmetric difference opration
# n= int(input())
# nE= set(map(int, input().split()))
# b= int(input())
# bF= set(map(int, input().split()))
# c= nE.symmetric_difference(bF)
# print(len(c))

#Set mutations
# nA= int(input())
# A= set(map(int, input().split()))
# n= int(input())
# for j in range(n):
#     nB= input().split()
#     B= map(int, input().split())
#     if nB[0] =='intersection_update':
#         A.intersection_update(B)
#     elif nB[0]== 'update':
#         A.update(B)
#     elif nB[0]== 'symmetric_difference_update':
#         A.symmetric_difference_update(B)
#     elif nB[0]== 'difference_update':
#         A.difference_update(B)
# print(sum(A))

#Caption's Room
# k= int(input())
# rn= list(map(int, input().split()))
# rn2= set(rn)
# c= (k*sum(rn2))-sum(rn)
# captinR= c//(k-1)
# print(captinR)

#Check subset
# T= int(input())
# for i in range(T):
#     nA= int(input())
#     A= set(map(int,input().split()))
#     nB= int(input())
#     B= set(map(int,input().split()))
#     print(A.issubset(B))

#Check strict superset
# A= set(map(int,input().split()))
# n= int(input())
# result= True
# for i in range(n):
#     other= set(map(int,input().split()))
#     if len(A)<= len(other):
#         result= False
#     if not other.issubset(A):
#         result= False
# print(result)

#collections.counter
# from collections import Counter
# x= int(input())
# s= Counter(map(int, input().split()))
# n= int(input())
# money=0
# for i in range(n):
#     size, xi= map(int,input().split())
#     if size in s and s[size]>0:
#         s[size]-=1
#         money+=xi
# print(money)


#DefaultDict Tutorial
# from collections import defaultdict
# n,m= map(int, input().split())

# d = defaultdict(list)
# for i in range(1,n+1):
#     d[input()].append(i)

# for i in range(1,m+1):
#     B=input()

#     if len(d[B]) > 0:
#         print(" ".join(str(c) for c in d[B]))
#     else:
#         print(-1)

#Collections.namedtuple
# from collections import namedtuple
# n= int(input())
# header= input().split()
# sumM= 0
# for i in range(n):
#     students= namedtuple('student', header)
#     MARKS, CLASS, NAME, ID = input().split()
#     student = students(MARKS, CLASS, NAME, ID)
#     sumM += int(student.MARKS)
# print(sumM / n)

#collections.deque
# from collections import deque
# d= deque()
# n= int(input())
# for i in range(n):
#     a=list(input().split())
#     if a[0]== 'append':
#         d.append(int(a[1]))
#     elif a[0]== 'pop':
#         d.pop()
#     elif a[0]== 'popleft':
#         d.popleft()
#     elif a[0]== 'appendleft':
#         d.appendleft(int(a[1]))
# for i in d:
#     print(i, end=' ')

#collection.orderedDict
# from collections import OrderedDict
# d= OrderedDict()
# n= int(input())
# for i in range(n):
#     a= input().split()
#     aName= " ".join(a[:-1])
#     aPrice= int(a[-1])
#     if (d.get(aName)):
#         d[aName]+= aPrice
#     else:
#         d[aName]= aPrice
# for i in d.keys():
#     print(i, d[i])

#Word order
# n= int(input())
# counter_dict = {}
# list= []

# for i in range(n):
#   a= input()
#   list.append(a)
#   if a in counter_dict:
#     counter_dict[a] += 1
#   else:
#     counter_dict[a] = 1

# print(len(counter_dict))
# print(' '.join([str(counter_dict[a]) for a in counter_dict]))

#Pilling_up
# from collections import deque
# n= int(input())
# for i in range(n):
#     f= True
#     input()
#     a= deque(map(int, input().strip().split()))
#     if(a[0] >= a[-1]):
#         max =a.popleft()
#     else:
#         max =a.pop()
#     while a:
#         if(len(a)==1):
#             if(a[0] <= max):
#                 break
#             else:
#                 f= False
#                 break
#         else:
#             if(a[0]<=max and a[-1]<=max):
#                 if(a[0]>=a[-1]):
#                     max =a.popleft()
#                 else:
#                     max =a.pop()
#             elif(a[0]<=max):
#                 max =a.popleft()
#             elif(a[-1]<=max):
#                 max =a.pop()
#             else:
#                 f= False
#                 break
#     if f:
#         print("Yes")
#     else:
#         print("No")

#Company Logo
# import math
# import os
# import random
# import re
# import sys
# import collections
# if __name__ == '__main__':
#     s = sorted(input().strip())
#     s_counter =collections.Counter(s).most_common()
#     s_counter =sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
#     for i in range(0, 3):
#         print(s_counter[i][0], s_counter[i][1])

#calender modul
# import calendar
# MM, DD, YYYY= map(int, input().split())
# c= calendar.weekday(YYYY, MM, DD)
# dayName= calendar.day_name[c]
# print(dayName.upper())

#time delta
# import math
# import os
# import random
# import re
# import sys
# from datetime import datetime
# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
#     return str(int(abs((t1-t2).total_seconds())))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input())
#     for t_itr in range(t):
#         t1 = input()
#         t2 = input()
#         delta = time_delta(t1, t2)

#exceptions
# T= int(input())
# for i in range(T):

#     try:
#         a,b= map(int,input().split())
#         print (a//b)
#     except (ZeroDivisionError,ValueError)  as e:
#          print ("Error Code:",e)

#zipped
# n,x= map(int, input().split())
# list=[]
# for i in range(x):
#     marks= map(float,input().split())
#     list.append(marks)
# s=zip(*list)
# for j in s:
#     ave= sum(j)/x
#     print(ave)

#Athlete Sort
# import math
# import os
# import random
# import re
# import sys
# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())
#     arr.sort(key = lambda x : x[k])
#     for i in arr:
#         print(*i,sep=' ')

#ginorts
#S = input()
#print(*sorted(S, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

#Map and Lambda function
# cube = lambda x: x**3
# def fibonacci(n):
#     # return a list of fibonacci numbers
#     list1=[0,1]
#     for i in range(2,n):
#         list1.append(list1[i-1]+list1[i-2])
#     return list1[:n]
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))

#Detect Floating Point Number
# import re
# for i in range(int(input())):
#     print(bool(re.match(r'^[+-]?\d*?\.{1}\d+$',input())))

#Re.split()
# regex_pattern = r",|\."
# import re
# print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()
# import re
# a= re.search(r'([A-Za-z0-9])\1+',input())
# if a:
#     print (a.group(1))
# else:
#     print (-1)

#Re.findall() & Re.finditer()
# import re
# a = re.findall(r'(?<=[^aeiouAEIOU ])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU ])',input())
# if a:
#     for i in a:
#         print (i)
# else:
#     print (-1)

#Re.start() & Re.end()
# S =input()
# k =input()
# import re
# a= re.compile(k)
# r=a.search(S)
# if not r:
#     print("(-1, -1)")
# while r:
#     print(f'{r.start(), r.end() - 1}')
#     r =a.search(S,r.start() + 1)

#Regex Substitution
# import re
# def substitution(m):
#     if m.group(1) == '&&':
#         return 'and'
#     else:
#         return 'or'
# n=int(input())
# for _ in range(n):
#     print(re.sub(r"(?<= )(\|\||&&)(?= )", substitution,input()))

#Validating Roman Numerals
# thousand='M{0,3}'
# hundred ='(C[MD]|D?C{0,3})'
# ten ='(X[CL]|L?X{0,3})'
# num ='(I[VX]|V?I{0,3})'
# regex_pattern = r"%s%s%s%s$" % (thousand,hundred,ten,num)	# Do not delete 'r'.
# import re
# print(str(bool(re.match(regex_pattern, input()))))

#Validating phone Numbers
# import re
# n= int(input())
# for i in range(n):
#     if re.match(r'[789]\d{9}$',input()):
#         print('YES')
#     else:
#         print('NO')

#Validating and Parsing Email Address
# import re
# n=int(input())
# for i in range(n):
#     name, email= input().split()
#     a= "<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
#     if bool(re.match(a,email)):
#         print(name, email)

#Hex color Code
# import re
# n= int(input())
# for i in range(n):
#     a=input()
#     t= a.split()
#     if len(t)>1 and "{" not in t:
#         for i in re.findall('#[0-9a-fA-F]{3,6}', a):
#             print(i)

#HTML parser,PART1
# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start :", tag)

#         for i in attrs:
#             print("-> %s > %s"%(i[0],i[1]))
#     def handle_endtag(self, tag):
#         print("End   :", tag)
#     def handle_startendtag(self, tag, attrs):
#         print("Empty :", tag)
#         for i in attrs:
#             print("-> %s > %s"%(i[0],i[1]))
# d= [input() for i in range(int(input()))]
# modd= ''.join(d)
# parser = MyHTMLParser()
# parser.feed(modd)

#HTML parser,PART2
# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, d):
#         if ('\n' not in d):
#             print('>>> Single-line Comment')
#             print(d)
#         elif ('\n' in d):
#             print('>>> Multi-line Comment')
#             print(d)
#     def handle_data(self, d):
#         if (d !='\n'):
#             print('>>> Data')
#             print(d)
# h= ""
# n=int(input())
# for i in range(n):
#     h+= input().rstrip()
#     h+= '\n'
# parser = MyHTMLParser()
# parser.feed(h)
# parser.close()

#Detect HTML Tags, Attributes and Attribute Values
# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         for a in attrs:
#             print("-> {} > {}".format(a[0], a[1]))
#     def handle_startendtag(self, tag, attrs):
#         print(tag)
#         for a in attrs:
#             print("-> {} > {}".format(a[0], a[1]))
# html = ""
# n=int(input())
# for i in range(n):
#     html += input().rstrip()
#     html += '\n'
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()

#Validating UID
# import re
# for i in range(int(input())):
#     n=input().strip()
#     if n.isalnum() and len(n) == 10:
#         if bool(re.search(r'(.*[A-Z]){2,}',n)) and bool(re.search(r'(.*[0-9]){3,}',n)):
#             if re.search(r'.*(.).*\1+.*',n):
#                 print('Invalid')
#             else:
#                 print('Valid')
#         else:
#             print('Invalid')
#     else:
#         print('Invalid')

#Validating Credit Card Numbers
# import re
# n= int(input().strip())
# for i in range(n):
#     num = "".join(input())
#     if (re.match(r'^[456]', num) and(re.match(r'([\d]{4}-){3}[\d]{4}$', num) or re.match(r'[\d]{16}', num)) and not re.search(r'(\d)\1{3,}', num.replace("-", ""))):
#         print("Valid")
#     else:
#         print("Invalid")

#Validating Postal Codes
# regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.
# import re
# P = input()

# print (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script
# import math
# import os
# import random
# import re
# import sys
# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
# matrix = []
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# matrix = list(zip(*matrix))
# a= str()
# for i in matrix:
#     for char in i:
#         a+= char
# print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ',a))

#find the score
# import sys
# import xml.etree.ElementTree as etree
# def get_attr_number(node):
#     a= 0
#     for i in node:
#         a=a+ get_attr_number(i)
#     return a+ len(node.attrib)
# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))

#Find the Maximum depth
# import xml.etree.ElementTree as etree
# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     level += 1
#     if (maxdepth < level):
#         maxdepth = level
#     for i in elem:
#         depth(i, level)
# if __name__ == '__main__':
#     n = int(input())
#     xml = ""
#     for i in range(n):
#         xml =  xml + input() + "\n"
#     tree = etree.ElementTree(etree.fromstring(xml))
#     depth(tree.getroot(), -1)
#     print(maxdepth)

#Standardize Mobile Number Using Decorators
# def wrapper(f):
#     def fun(l):
#         # complete the function
#         num = ['+91' + ' ' + i[-10:-5] + ' ' + i[-5:] for i in l]
#         f(num)
#     return fun
# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')
# if __name__ == '__main__':
#     l = [input() for _ in range(int(input()))]
#     sort_phone(l)

#Name Directory
# import operator
# def person_lister(f):
#     def inner(people):
#         return map(f, sorted(people, key=lambda x:int(x[2])))
#     return inner
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')

#Arrays
# import numpy
# def arrays(arr):
#     a= numpy.array(arr, float)
#     b=a[::-1]
#     return b
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

#Shape and Reshape
# import numpy
# arr = input().strip().split(' ')
# a= numpy.array(arr, int)
# new_arr= numpy.reshape(a,(3,3))
# print(new_arr)

#Transpose and Flatten
# import numpy
# n,m= map(int, input().split())
# a=numpy.array([input().strip().split() for _ in range(n)], int)
# print(a.transpose())
# print(a.flatten())

#Concatenate
# import numpy
# n,m,p= map(int, input().split())
# arr1= numpy.array([input().split() for i in range(n)], int)
# arr2= numpy.array([input().split() for i in range(m)], int)
# print(numpy.concatenate((arr1, arr2), axis= 0))

#Zeros and Ones
# import numpy
# m= tuple(map(int, input().split()))
# print(numpy.zeros((m),int))
# print(numpy.ones((m),int))

#Eye and identity
# import numpy
# numpy.set_printoptions(legacy='1.13')
# n,m= map(int, input().split())
# print(numpy.eye(n,m))

#Array Mathematics
# import numpy
# n,m = map(int, input().split())
# a= numpy.array([input().split() for i in range(n)], int)
# b= numpy.array([input().split() for i in range(n)], int)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(a**b)

#Floor Ceil and Rint
# import numpy
# numpy.set_printoptions(legacy='1.13')
# a= numpy.array(input().split(), float)
# print(numpy.floor(a))
# print(numpy.ceil(a))
# print(numpy.rint(a))

#Sum and Prod
# import numpy
# n, m = map(int, input().split())
# arr= numpy.array([input().split() for i in range(n)], int)
# p= numpy.sum(arr, axis=0)
# print(numpy.prod(p))

#Min and Max
# import numpy
# n,m =map(int, input().split())
# arr= numpy.array([input().split() for i in range(n)], int)
# min1= numpy.min(arr, axis=1)
# print(numpy.max(min1))

#Min Var and Std
# import numpy
# n, m =map(int, input().split())
# arr= numpy.array([input().split() for i in range(n)], int)
# print(numpy.mean(arr,axis=1))
# print(numpy.var(arr,axis=0))
# numpy.set_printoptions(legacy='1.13')
# print(round(numpy.std(arr), 11))

#Dot and Cross
# import numpy
# n= int(input())
# a= numpy.array([input().split() for i in range(n)], int)
# b= numpy.array([input().split() for i in range(n)], int)
# print(numpy.dot(a, b))

#Inner and Outer
# import numpy
# a= numpy.array(input().split(), int)
# b= numpy.array(input().split(), int)
# print(numpy.inner(a,b))
# print(numpy.outer(a,b))

#Polynomials
# import numpy
# cp= list(map(float,input().split()))
# x= float(input())
# print(numpy.polyval(cp, x))

#Linear Algebra
# import numpy
# n= int(input())
# a= numpy.array([input().split() for i in range(n)], float)
# print(round(numpy.linalg.det(a),2))

##--------------------------------------------------------------------------------------------------------
##PROBLEM2:

#Birthday cake candles
# import math
# import os
# import random
# import re
# import sys
# def birthdayCakeCandles(candles):
#     # Write your code here
#     maxcand = max(candles)
#     t= 0
#     for i in range(len(candles)):
#         if candles[i] == maxcand:
#             t+=1
#     return t
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     candles_count = int(input().strip())
#     candles = list(map(int, input().rstrip().split()))
#     result = birthdayCakeCandles(candles)
#     fptr.write(str(result) + '\n')
#     fptr.close()

#Kangaroo
# import math
# import os
# import random
# import re
# import sys
# def kangaroo(x1, v1, x2, v2):
#     if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0:
#         return "YES"
#     else:
#         return "NO"
#     x1,v1,x2,v2 = map(int,input().split())
#     total= kangaroo(x1, v1, x2, v2)
#     print(total)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     x1 = int(first_multiple_input[0])

#     v1 = int(first_multiple_input[1])

#     x2 = int(first_multiple_input[2])

#     v2 = int(first_multiple_input[3])

#     result = kangaroo(x1, v1, x2, v2)

#     fptr.write(result + '\n')

#     fptr.close()


#strange advertising
# import math
# import os
# import random
# import re
# import sys
# def viralAdvertising(n):
#     a=5
#     bt = 0
#     for i in range(n):
#         b = a//2
#         bt += b
#         a = b*3
#     return bt
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     result = viralAdvertising(n)

#     fptr.write(str(result) + '\n')

#     fptr.close()


#recursive digit sum
# import math
# import os
# import random
# import re
# import sys
# def superDigit(n, k):
#     return 1 + (k * sum(int(i) for i in n) - 1) % 9
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = first_multiple_input[0]

#     k = int(first_multiple_input[1])

#     result = superDigit(n, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#insertion sort1
# def insertionSort1(n, arr):
#     import math
# import os
# import random
# import re
# import sys
# def insertionSort1(n, arr):
#     # Write your code here
#     key= arr[-1]
#     i= n-2
#     while (key < arr[i] and i >= 0):
#         arr[i+1] = arr[i]
#         print(*arr)
#         i -= 1
#     arr[i+1] = key
#     print(*arr)

# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))
#     insertionSort1(n, arr)

#insertion sort2
# import math
# import os
# import random
# import re
# import sys
# def insertionSort2(n, arr):
#     # Write your code here
#     for n in range(1,n):
#         i = arr[n]
#         while n>0:
#             if i > arr[n-1]:
#                 arr[n] = i
#                 print(*arr)
#                 break
#             else:
#                 arr[n] =arr[n-1]
#             n-=1
#         else:
#             arr[0] = i
#             print(*arr)
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))
#     insertionSort2(n, arr)

##--------------------------------------------------------------------------------------------------------
