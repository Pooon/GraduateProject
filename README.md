# GraduateProject

Base Url: http://120.24.56.172:5000/

##User

###Log in: '/login'
>params:  
>  'email': char  
>  'password': char  
>  'remember_me' : boolean  

>response:  
>  '202' : Log in successfully  
>  '203' : Invalid username or password  

###Register:
>params:  
>  'email': char  
>  'username' : char  
>  'password' : char  

>response:  
>  '202' : Register successfully  
>  '203' : Fail  
