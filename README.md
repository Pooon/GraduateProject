# GraduateProject

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
