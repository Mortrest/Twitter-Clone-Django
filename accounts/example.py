import re
# l = ['0x']

# s = '-'.join(l)

# print(s)

# pattern = re.compile('[0-9]+x')
# result = pattern.findall(s)

# result = [i.rstrip('x') for i in result]

# print(result)

# result = 'x'.join(result)
# result = result + 'x'
# pattern = re.compile('[0-9]+x')
# result = pattern.findall(result)

# result = [i.rstrip('x') for i in result]

# print(result)
# l = '0x2x23x'
# pattern = re.compile('[0-9]+x')
# likeList = pattern.findall(l)
# likeList = [i.rstrip('x') for i in likeList]
# pk = 3
# #Like Logic
# try:
#     q = 1
# #Ok she inja
# except:
#     print('hello')
# else:
#     if (str(pk)) in likeList:
#         likeList.remove(str(pk))
#         print('Yaft shod')
#         print(likeList)
#         likeList = 'x'.join(likeList)
#         likeList = likeList + 'x'
#         # Inja bayad save koni hale 

#     else:
#         print('Yaft nashod')
#         likeList.append(str(pk))
#         print(likeList)
#         likeList = 'x'.join(likeList)
#         likeList = likeList + 'x'
#         print(likeList)


# def likeView(request, pk):
# 	post = Post.objects.get(id=pk)
# 	user = Profile.objects.get(id=request.user.id)
    
#     try:
#         z = 0
#     #Ok she inja
#     except:
#         print('hello')
#     else:
#         if str(pk) in likeList:
#             likeList.remove(str(pk))
#             likeList = 'x'.join(likeList)
#             likeList = likeList + 'x'   
#             user.likeList = likeList
#             user.save()        
#             post.likes -= 1
#             post.save()
#         else:
#             likeList.append(str(pk))
#             likeList = 'x'.join(likeList)
#             likeList = likeList + 'x'   
#             user.likeList = likeList
#             user.save()
#             post.likes += 1
#             post.save()

#         return redirect('home')

# s = 'awdA21op2@awdjASDEijo@'

# pattern = re.compile('[A-Za-z0-9]+@')
# result = pattern.findall(s)
# result = [i.rstrip('@') for i in result]
# print(result)
# result = '@'.join(result)
# result = result + '@'
# print(result)


def tweetFunction(request):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    new_comment = None
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = UserClass.objects.get(user=request.user)

            new_comment.save()
    else:
        form = CommentForm()

    context = {
        'question':question,
        'comments':comments,
        'form':form
    }
    return render(request,'blog/comments.html',context)


class Profile(models.Model):
    user = models.OneToOneField(User)


class Post(models.Model):
    user = models.ManyToManyField(Profile)

q = Post
q.save()
#Tweet Function
for i in followList:
    q.user.add(Profile.objects.get(username=i))

# yadet nare be khode bande khodash add koni
q.user.add({% loop %})
Post.objects.get(id=pk).user.add({% loop %})



#View Function in html
{% for i in profile.post_set.all %}
{{ i. }}




def addTweet(request):
	form = TweetForm()
	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
            a = body=form.cleaned_data.get('body')
            q = Post.objects.create(body=a)
            q.author = request.user
            q.user.add(request.user)
            user = Profile.objects.get(id=request.user.id)
            pattern = re.compile('[A-Za-z0-9]+@')
            followList = pattern.findall(user.followList)
            followList = [i.rstrip('@') for i in followList]
            for i in followList:
                q.user.add(username=i)
                q.save()

            return redirect('home')
        else:
            form = TweetForm()
def commentView(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data.get('body')
            q = Comments.objects.create(body=a)
            q.post = post
            q.user = request.user
            #q = Comments(user=request.user)
            # Post ro moshakhas kon
            q.save()
            return redirect('detail',pk=pk)
        else:
            form=CommentForm()





                                    <div class="box22 d-flex align-self-center justify-content-around flex-column " style="height: 4rem; width: 90%; border-bottom: 2px solid  rgba(248, 246, 246, 0.05) ">
                            <div class=" d-flex mt-2 align-self-start">
                                <img src="{% static 'users/2.png'%}" width="20" height="20">
                                <div style="color:white; font-size:16px;font-weight: 600;font-family: inherit;">&nbsp;David</div>
                            </div>
                            <div class="align-self-start" style="color: rgb(113,121,132);">david@gmail.com</div>
                        </div>
                        <div class="box22 d-flex align-self-center justify-content-around flex-column " style="height: 4rem; width: 90%; rgba(248, 246, 246, 0.05) ">
                            <div class=" d-flex mt-2 align-self-start">
                                <img src="{% static 'users/3.png' %}" width="20" height="20">
                                <div style="color:white; font-size:16px;font-weight: 600;font-family: inherit;">
                                    <a href="
                                    " style="color: white; text-decoration: white;">&nbsp;David</a></div>
                            </div>
                            <div class="align-self-start" style="color: rgb(113,121,132);">david@gmail.com</div>
                        </div>

















                        {% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitter</title>
    <link rel="icon" type="image/png" href="{% static 'logo.png' %}">
    <link rel="stylesheet" href="{% static 'Bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'fontawesom/css/all.css' %}">
</head>
<body>
    <style>
    body{background-color: rgb(22,32,42); }
    .header{ height: 3.5rem; font-size: 14px; width: auto;
        border-bottom-width:2px; border-bottom-style: solid; border-bottom-color: rgba(248, 246, 246, 0.05);}
    .box1{background-color:rgb(32,42,52); height: 7rem; border-radius: 12px; width: 100%;}

    </style>
    <script src="{% static 'JS/Jquery.js' %}"></script>
    <script src="{% static 'JS/popper.js' %}"></script>
    <script src="{% static 'Bootstrap/js/bootstrap.min.js' %}"></script>
    <div class="header row container-fluid align-items-center  ">
        <div class="col-3">
            <a href="{% url 'home' %}" class="ml-4" href="#" style="text-decoration: none; color: rgb(113,121,132);font-size: 20px;">
                <strong>         Home</strong>
            </a>
        </div>
        <div class="col-3 offset-6 text-center">
            <a href="#" style="color:rgb(113,121,132);font-weight: 600;">Creat a Tweet
            </a>&nbsp;&nbsp;&nbsp;
            <a href="#" style="color: rgb(113,121,132);font-weight: 600;">Settings
            </a>&nbsp;&nbsp;&nbsp;
            <a href="{% url 'logout' %}" style="color:rgb(113,121,132);font-weight: 600;text-decoration: none;">Logout
            </a>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row ">
            <div class="leftbar row col-3 mt-1 " style=" height:30rem; border-right: 2px solid rgba(248, 246, 246, 0.05)">
                <a href="{% url 'home' %}"><i class="fab fa-twitter mt-2 ml-3" style="color: rgb(0, 132, 255); font-size: 54px;"></i></a>
                
                <div class="mt-2 ml-3" style="font-size: 32px; color: rgb(113,121,132);">
                   <a href="{% url 'home' %}" style="text-decoration: none;color: white;font-weight: 750;"> Twitter</a></div>
                   <div class="w-100"></div>
                   <div class="box1 align-content-start row col-11 ml-3" style="border-radius: 1rem; height: 24rem; background-color:rgb(45,55,65)">
                       <div class="h4 mt-2" style="font-weight: bold; color:white">Profile</div>
                       <div class="w-100"></div>

                    <img class=" mt-2 " src="{% static 'users/1.png' %}" height="75" width="75"  alt="...">&nbsp;
                    <div class="align-self-center ml-2 mt-3" style="font-weight: 600; font-size: 26px; color:rgba(255, 255, 255, 0.87)"><a href="{% url 'profile' request.user.id %}" style="text-decoration: none;color: bisque;"> @{{profile.username}}</a></div>
                    <div class="w-100"></div>
                    <div class="mt-3 ml-1" style="color:rgb(216, 218, 221) ;font-size: 16px;font-weight: 600;">{{ profile.bio }} </div>



                    <div class="position-static">
                    <div class="mt-5 ml-1" style="color:rgb(113,121,132) ;">Followers&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Following</div>
                    <div class="w-100"></div>
                    <div class=" ml-4" style="color:white ; margin-top:-8px; font-size: 2rem; font-weight: bold;">{{ profile.followers }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ profile.followings }}</div>
                </div>
                {% block content %}

                {% endblock %}         
            </div>
        </div>


<!--Here-->



        <div class="mainbar col-6 mt-3 row justify-content-between align-items-start"  style=" height:28rem; border-right: 2px solid rgba(248, 246, 246, 0.05)">
            <div class="align-self-start ml-4" style="font-weight: bold; color: white; font-size: 22px;">Tweets</div>
            <div class="" style="color: white; font-size: 16px;">1-3 of 4</div>
            <div class="w-100"></div>
            <div class="box1 ml-4 justify-content-center">
                <div class="box11 d-flex justify-content-between ml-2 " style="width: 97%; height: 1.6rem; border-bottom: 2px solid rgba(248, 246, 246, 0.05); ">
                    <div class="d-flex"
                    ><img class=" mt-1 " src="{% static 'users/1.png' %}" height="15" width="15"  alt="...">&nbsp;
                    <div class=" mt- " style="color: white; font-size: 14px; font-weight: bold;" >admin</div></div>
                </div>
                <form action="">
                    {% csrf_token %}
                    <div class="form-group" >
                    {% for field in form %}
                        {{ field }}
                    {% endfor %}   
                        <button class="btn btn-sm btn-primary float-right mr-3 mt-1" type="submit">Tweet</button>
                    </div>  
                </form>                
            </div>
            <div class="w-100"></div>
            <div class="box1 ml-4 justify-content-center">
                <div class="box11 d-flex justify-content-between ml-2 " style="width: 97%; height: 1.9rem; border-bottom: 2px solid rgba(248, 246, 246, 0.05); ">
                    <div class="d-flex"
                    ><img class=" mt-1 " src="{% static 'users/1.png' %}" height="20" width="20"  alt="...">&nbsp;
                    <div class=" mt- " style="color: white;" >admin</div></div>
                    <div class="d-flex">
                        <i class="far fa-window-close align-self-center" style=" font-size:12px; color: grey;"></i>
                    </div>
                </div>
                <div class="mt-2 ml-2" style="color:rgb(144,155,159);">WELCOME EVERYONE</div>
        
                <div class="d-flex mt-2 justify-content-between align-content-end">
                    <div class="align-self-end">​<i class="fa fa-heart ml-2" style="color: indianred; font-size: 12px;"></i><p style="color:rgb(0, 255, 191); font-size: 12px;" class="d-inline" > 1 like(s)</p><i class="far fa-comment ml-2" style="font-size: 12px; color:rgb(113,121,132)"></i><p style="color:rgb(113,121,132); font-size: 12px;" class="d-inline" > 0 comment(s)</p></div>
                    <div class="mr-2" style="font-size: 12px; color:rgb(113,121,132)">09:19 Monday,01,06,20</div></div>                  
            </div>
            
            <div class="w-100"></div>
            <div class="box1 ml-4 justify-content-center">
                <div class="box11 d-flex justify-content-between ml-2 " style="width: 97%; height: 1.9rem; border-bottom: 2px solid rgba(248, 246, 246, 0.05); ">
                    <div class="d-flex"
                    ><img class=" mt-1 " src="users/1.png" height="20" width="20"  alt="...">&nbsp;
                    <div class=" mt- " style="color: white;" >admin</div></div>
                    <div class="d-flex">
                        <i class="far fa-window-close align-self-center" style=" font-size:12px; color: grey;"></i>
                    </div>
                </div>
                <div class="mt-2 ml-2" style="color:rgb(144,155,159);">WELCOME EVERYONE</div>
        
                <div class="d-flex mt-2 justify-content-between align-content-end">
                    <div class="align-self-end">​<i class="fa fa-heart ml-2" style="color: indianred; font-size: 12px;"></i><p style="color:rgb(0, 255, 191); font-size: 12px;" class="d-inline" > 1 like(s)</p><i class="far fa-comment ml-2" style="font-size: 12px; color:rgb(113,121,132)"></i><p style="color:rgb(113,121,132); font-size: 12px;" class="d-inline" > 0 comment(s)</p></div>
                    <div class="mr-2" style="font-size: 12px; color:rgb(113,121,132)">09:19 Monday,01,06,20</div></div>                  
            </div>

            <div class="w-100"></div>
            <div class="d-flex justify-content-center" style="width: 100%;">
                <div><input class="" type="button" value="1" style="position: relative; top: 13px; background-color: rgb(60,69,100);border-radius: 3px;border: 1px solid white;color: white"></div>  
                <div class="ml-2"><input type="button" value="2" style="position: relative; top: 13px; background: none;border-radius: 3px; border: 1px solid white;color: white"></div> 
                <div class="ml-2"><input type="button" value="Next" style="position: relative; top: 13px; background: none;border-radius: 3px; border: 1px solid white;color: white"></div>
                <div class="ml-2"><input type="button" value="Last" style="position: relative; top: 13px; background: none;border-radius: 3px; border: 1px solid white;color: white"></div> 
            </div>
            </div>


<!--Inja-->
                <div class="rightbar row d-flex col-3 ml-3" style=" height:30rem;">
                            <div>
                                <form action="{% url 'search' %}" method="POST" style="border: seagreen; stroke: seagreen;">
                                    {% csrf_token %}
                                <input required name="search" class=" mt-3" type="text" style=" padding:10px; background-color: rgb(37,51,64); border-top-left-radius: 17px; border-bottom-left-radius: 17px;  height: 40px;  width: 16rem; border: none;border: seagreen;color: white;font-weight: 600;" placeholder="Search Twitter">

                                </form>
                            </div>
                            <div>
                                <i class="fa fa-search btn mt-3" style=" border-bottom-left-radius: 0px; border-top-left-radius: 0px; color: white;font-size: 24px; background-color: rgb(37,51,64); height: 40px; border-top-right-radius: 17px; border-bottom-right-radius: 17px; width: 3rem; padding: 7px;"></i>
                            </div>

                    <div class="w-100"></div>
                    <div style="color: white;">
                        <h2 style="font-weight: 600;font-family: inherit;">Trends</h2>
                    </div>
                    <div class="box12 d-flex align-content-end flex-column" style="width: 98%; border-radius: 15px; height: 16rem; background-color: rgb(45,55,65);">
                        <div class="box22 d-flex align-self-center" style="height: 3rem; width: 90%; border-bottom: 2px solid  rgba(248, 246, 246, 0.05) ">
                            <div class="align-self-center" style="color:rgb(198, 209, 216); font-size:22px;font-weight: 600;">Who to Follow</div>
                        </div>

                        {% for i in profile_last %}
                            {% if i.id != request.user.id %}
                                <div class="box22 d-flex justify-content-start align-self-center align-content-start" style="height: 3rem; width: 90%; border-bottom: 2px solid  rgba(248, 246, 246, 0.05) ">
                                    <img class="align-self-center" src="{% static 'users/1.png' %}" width="20" height="20">
                                    <div class="align-self-center" style="color:white; font-size:16px;font-weight: 600;font-family: inherit;">&nbsp;<a href="{% url 'profile' i.id %}" style="text-decoration: none; color: rgb(233, 227, 227);">{{ i.username }}</a></div>
                                </div>
                            {% endif %}

                        {% endfor %}


                </div>
                <div>
                    <p style="color: white;font-size: 16px">Terms, Privacy policy, Cookies, Ads, info, More <span style="color:rgb(128,137,146)">@2020 twitter, inc</span>
                    </p>
                </div>
               
                </div>
            </div>       
    </div>


</body>
</html>



























{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitter</title>
    <link rel="icon" type="image/png" href="{% static 'logo.png' %}">
    <link rel="stylesheet" href="{% static 'Bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'fontawesom/css/all.css' %}">
</head>
<body>
    <style>
    body{background-color: rgb(22,32,42); }
    .header{ height: 3.5rem; font-size: 14px; width: auto;
        border-bottom-width:2px; border-bottom-style: solid; border-bottom-color: rgba(248, 246, 246, 0.05);}
    .box1{background-color:rgb(32,42,52); height: 7rem; border-radius: 12px; width: 100%;}

    </style>
    <script src="{% static 'JS/Jquery.js' %}"></script>
    <script src="{% static 'JS/popper.js' %}"></script>
    <script src="{% static 'Bootstrap/js/bootstrap.min.js' %}"></script>
    <div class="header row container-fluid align-items-center  ">
        <div class="col-3">
            <a href="{% url 'home' %}" class="ml-4" href="#" style="text-decoration: none; color: rgb(113,121,132);font-size: 20px;">
                <strong>         Home</strong>
            </a>
        </div>
        <div class="col-3 offset-6 text-center">
            <a href="#" style="color:rgb(113,121,132);font-weight: 600;">Creat a Tweet
            </a>&nbsp;&nbsp;&nbsp;
            <a href="#" style="color: rgb(113,121,132);font-weight: 600;">Settings
            </a>&nbsp;&nbsp;&nbsp;
            <a href="{% url 'logout' %}" style="color:rgb(113,121,132);font-weight: 600;text-decoration: none;">Logout
            </a>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row ">
            <div class="leftbar row col-3 mt-1 " style=" height:30rem; border-right: 2px solid rgba(248, 246, 246, 0.05)">
                <a href="{% url 'home' %}"><i class="fab fa-twitter mt-2 ml-3" style="color: rgb(0, 132, 255); font-size: 54px;"></i></a>
                
                <div class="mt-2 ml-3" style="font-size: 32px; color: rgb(113,121,132);">
                   <a href="{% url 'home' %}" style="text-decoration: none;color: white;font-weight: 750;"> Twitter</a></div>
                   <div class="w-100"></div>
                   <div class="box1 align-content-start row col-11 ml-3" style="border-radius: 1rem; height: 24rem; background-color:rgb(45,55,65)">
                       <div class="h4 mt-2" style="font-weight: bold; color:white">Profile</div>
                       <div class="w-100"></div>

                    <img class=" mt-2 " src="{% static 'users/1.png' %}" height="75" width="75"  alt="...">&nbsp;
                    <div class="align-self-center ml-2 mt-3" style="font-weight: 600; font-size: 26px; color:rgba(255, 255, 255, 0.87)"><a href="{% url 'profile' request.user.id %}" style="text-decoration: none;color: bisque;"> @{{profile.username}}</a></div>
                    <div class="w-100"></div>
                    <div class="mt-3 ml-1" style="color:rgb(216, 218, 221) ;font-size: 16px;font-weight: 600;">{{ profile.bio }} </div>



                    <div class="position-static">
                    <div class="mt-5 ml-1" style="color:rgb(113,121,132) ;">Followers&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Following</div>
                    <div class="w-100"></div>
                    <div class=" ml-4" style="color:white ; margin-top:-8px; font-size: 2rem; font-weight: bold;">{{ profile.followers }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ profile.followings }}</div>
                </div>
                {% block content %}

                {% endblock %}         
            </div>
        </div>
            <div class="mainbar col-6 mt-3 row justify-content-between align-items-start"  style=" height:30rem; border-right: 2px solid rgba(248, 246, 246, 0.05)">
                <div class="align-self-start ml-4" style="font-weight: bold; color: white; font-size: 22px;">Tweets</div>
                {% if page_number == None %}

                    <div class="mt-1" style="color: white; font-size: 16px;font-weight: 600;">Page 1 of {{ num_pages }}</div>
                {% else %}
                    <div class="mt-1" style="color: white; font-size: 16px;font-weight: 600;">Page {{ page_number }} of {{ num_pages }}</div>
                {% endif %}




                
                {% if not profile.post_set.all.exists %}


                <div class="w-100 h-100 mt-4 mr-4" >
                <div class="w-100" ></div>
                <div class="box1 ml-4 justify-content-center mt-4" style="background-color: rgb(22, 32, 42);">
                    <div class="box11 d-flex justify-content-between ml-2 " style="width: 97%; height: 2.4rem;">
                        <div class="d-flex"
                        >
                        <div class="ml-1 mt-1" style="color: white;" >
                            <h2 class="">No Tweets...</h2>
                        </div>
                    </div>
                    </div>
                    </div>
                    </div>
                </div>
                {% endif %}
                {% for i in post %}

                    <div class="w-100"></div>
                    <div class="box1 ml-4 justify-content-center align-items-start">
                        <div class="box11 d-flex justify-content-between ml-2 " style="width: 97%; height: 2.4rem; border-bottom: 2px solid rgba(248, 246, 246, 0.05); ">
                            <div class="d-flex"
                            >
                            <a href="{% url 'profile' i.author.id %}" style="text-decoration: none;">
                            <img class=" mt-2 " src="{% static 'users/1.png' %}" height="20" width="20"  alt="...">&nbsp;
                            </a>
                            <div class="ml-1 mt-1 " style="color: white;" >
                                <a href="{% url 'profile' i.author.id %}" style="text-decoration: none; color: rgb(216, 205, 186); font-size: 16px;font-family:inherit;font-weight: 600;" >{{ i.author }}</a></div></div>
                            <div class="d-flex">
                                <a href="{% url 'deleteTweet' i.id %}">
                                <i class="far fa-window-close align-self-center" style=" font-size:12px; color: grey;"></i></a>
                            </div>
                        </div>
                        <a href="{% url 'detail' i.id %}" style="text-decoration: none;">
                        <div class="mt-1 ml-2" style="color:rgb(216, 218, 221);font-weight: 600;">{{ i.body }}</div>
                
                        </a>


<!-- Like&Comment Button -->

                        <div class="d-flex mt-3 justify-content-between align-content-end">
                            <div class="align-self-end" style="display: flex;">



                                <a  href="{% url 'like' i.id %}" style="text-decoration: none;">
                                    {% if i.id in likeList %}
                                        <i class="fa fa-heart ml-2 " style="color: indianred; font-size: 14px;"></i>
                                    {% else %}
                                        <i class="fa fa-heart ml-2 " style= "color:rgb(63, 69, 95);font-size: 14px; text-decoration: none;"></i>
                                    {% endif %}
                                    <p style="color:rgb(112, 128, 150); font-size: 14px; text-decoration: none;font-weight: 600;" class="d-inline" > {{i.likesCount}} Likes</p>    
                                </a> 

                            <form id="likebutton" method="POST" action="{% url 'like' i.id %}">
                            {% csrf_token %}
                            <input type="hidden">
                            </form>
                                
                                


                            <a href="{% url 'detail' i.id %}" style=" color:rgb(113,121,132); text-decoration: none;">
                                <i style=" font-size: 14px;" class="far fa-comment ml-3" ></i> 
                                <p style="color:rgb(112, 128, 150); font-size: 14px;font-weight: 600;" class="d-inline" > {{ i.comment_set.all.count }} Comments</p>

                            </a>
                            


                        </div>
                            <div class="mr-2" style="color:rgb(113,121,132);font-size: 14px;font-weight: 600;">{{i.dateCreated}}</div>
                        </div>                  




                    </div>

                {% endfor %}



                {% if profile.post_set.all.exists %}
                    
                <div class="w-100"></div>
                <div class="d-flex justify-content-center" style="width: 100%;">
                    {% if post.has_previous %}
                        <div class="ml-2">
                            <a href="{% url 'home' %}?page={{ post.previous_page_number }}">
                            <input type="button" value="Previous" style="background: none;border-radius: 3px; border: 1px solid rgb(113,121,132);color: rgb(112, 128, 150)"></a></div>
                    {% endif %}
                      
                        {% for i in n %}
                            <div class="ml-2">
                                <a href="{% url 'home' %}?page={{ i }}">

                                    <input type="button" value="{{ i }}" 
                                    style="background-color: rgb(37,51,64);border-radius: 3px;border: 1px solid rgb(113,121,132);color: rgb(112, 128, 150)">   
                                
                            </a></div>  
                        {% endfor %}

                    {% if post.has_next %} 
                        <div class="ml-2">
                            <a href="{% url 'home' %}?page={{ post.next_page_number }}">
                            <input type="button" value="Next" style="background: none;border-radius: 3px; border: 1px solid rgb(113,121,132);color: rgb(112, 128, 150)"></a></div>
                    {% endif %}



                </div>
                </div>
                {% endif %}




<!--Inja-->
                <div class="rightbar row d-flex col-3 ml-3" style=" height:30rem;">
                            <div>
                                <form action="{% url 'search' %}" method="POST" style="border: seagreen; stroke: seagreen;">
                                    {% csrf_token %}
                                <input required name="search" class=" mt-3" type="text" style=" padding:10px; background-color: rgb(37,51,64); border-top-left-radius: 17px; border-bottom-left-radius: 17px;  height: 40px;  width: 16rem; border: none;border: seagreen;color: white;font-weight: 600;" placeholder="Search Twitter">

                                </form>
                            </div>
                            <div>
                                <i class="fa fa-search btn mt-3" style=" border-bottom-left-radius: 0px; border-top-left-radius: 0px; color: white;font-size: 24px; background-color: rgb(37,51,64); height: 40px; border-top-right-radius: 17px; border-bottom-right-radius: 17px; width: 3rem; padding: 7px;"></i>
                            </div>

                    <div class="w-100"></div>
                    <div style="color: white;">
                        <h2 style="font-weight: 600;font-family: inherit;">Trends</h2>
                    </div>
                    <div class="box12 d-flex align-content-end flex-column" style="width: 98%; border-radius: 15px; height: 16rem; background-color: rgb(45,55,65);">
                        <div class="box22 d-flex align-self-center" style="height: 3rem; width: 90%; border-bottom: 2px solid  rgba(248, 246, 246, 0.05) ">
                            <div class="align-self-center" style="color:rgb(198, 209, 216); font-size:22px;font-weight: 600;">Who to Follow</div>
                        </div>

                        {% for i in profile_last %}
                            {% if i.id != request.user.id %}
                                <div class="box22 d-flex justify-content-start align-self-center align-content-start" style="height: 3rem; width: 90%; border-bottom: 2px solid  rgba(248, 246, 246, 0.05) ">
                                    <img class="align-self-center" src="{% static 'users/1.png' %}" width="20" height="20">
                                    <div class="align-self-center" style="color:white; font-size:16px;font-weight: 600;font-family: inherit;">&nbsp;<a href="{% url 'profile' i.id %}" style="text-decoration: none; color: rgb(233, 227, 227);">{{ i.username }}</a></div>
                                </div>
                            {% endif %}

                        {% endfor %}


                </div>
                <div>
                    <p style="color: white;font-size: 16px">Terms, Privacy policy, Cookies, Ads, info, More <span style="color:rgb(128,137,146)">@2020 twitter, inc</span>
                    </p>
                </div>
               
                </div>
            </div>       
    </div>


</body>
</html> 