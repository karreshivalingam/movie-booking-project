#!/usr/bin/env python
# coding: utf-8

# In[ ]:


global f
f = 0
  
#this t_movie function is used to select movie name 
def t_movie():
    global f
    f = f+1
    print("which movie do you want to watch?")
    print("1,Acharya ")
    print("2,vakeel saab ")
    print("3,chicchore")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
      # in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater 
      center()
      theater()
      return 0
    if f == 1:
      theater()
  
# this theater function used to select screen 
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("chosse your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    timing(a)
  
# this timing function used to select timing for movie 
def timing(a):
    time1 = {
        "1": "11.00-2.00",
        "2": "2.15-4.15",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "11.00-2.00",
        "2": "2.15-4.15",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time3 = {
        "1": "11.00-2.00",
        "2": "2.15-4.15",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successfull!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successfull!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successfull!, enjoy movie at "+x)
    return 0
  
  
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
  
  
def center():
    print("which theater do you wish to see movie? ")
    print("1,Asian Uppal")
    print("2,Miraj cinemas")
    print("3,Inox")
    print("4,back")
    a = int(input("choose your option: "))
    movie(a)
    return 0
  
# this function is used to select city 
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1,Uppal")
    print("2,L.B Nagar")
    print("3,Juble hills")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    else:
      print("wrong choice")
  
  
city() # it calls the function city


# In[ ]:




