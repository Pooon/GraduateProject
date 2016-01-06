# API List

Base Url: http://120.24.56.172:5000/

##User

###Log in: '/login'
<b> params: </b>    
>  'email': char  
>  'password': char  
>  'remember_me' : boolean  

<b> response:</b>  
>  '200' : Log in successfully  
>  '403' : Invalid username or password  

###Register: '/register'
<b> params: </b>    
>  'email': char  
>  'username' : char  
>  'password' : char  

<b> response:</b>    
>  '200' : Register successfully  
>  '403' : Fail  


=========================

#数据库

###User
user      |
----------|
user_id   | 
username  |
pwd_hash  |
email     |

###Course
course    |
----------|
course_id |
course_name|
course_abstract(简介)|
tutor_id|
catogory_id|

###Category
catrgory|
--------|
category_id|
title|

###Lecture
lecture|
-------|
lecture_id|
lecture_name|
order|
lecture_abstract|
course_id|
video_url|


