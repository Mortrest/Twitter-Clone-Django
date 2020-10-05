from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
import re


#homePage View
def homePage(request):
    context = {}
    return render(request,'accounts/index.html',context)


#Tweet Function (UnTest)
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


#Follow Function (UnTest)
def followFunction(request, pk):
    target = Profile.objects.get(id=pk)
    user = Profile.objects.get(id=request.user.id)
    pattern = re.compile('[A-Za-z0-9]+@')
    followList = pattern.findall(user.followList)
    followList = [i.rstrip('@') for i in followList]
    try:
        q = 1
    except:
        a = 1
    else:
        if target.username in followList:
            followList.remove(target.username)
            followList = '@'.join(followList)
            followList = followList + '@'   
            user.followList = followList
            user.followings -= 1
            user.save()        
            target.followers -= 1
            target.save()
        else:
            followList.append(target.username)
            followList = '@'.join(followList)
            followList = followList + '@'   
            user.followList = followList
            user.followings += 1
            user.save()        
            target.followers += 1
            target.save()

        return redirect('home')



#Like Function (UnTest)
def likeFunction(request, pk):
    post = Post.objects.get(id=pk)
    user = Profile.objects.get(id=request.user.id)
    pattern = re.compile('[0-9]+x')
    likeList = pattern.findall(user.likeList)
    likeList = [i.rstrip('x') for i in likeList]
    try:
        z = 0
    #Ok she inja
    except:
        w = 0
    else:
        if str(pk) in likeList:
            likeList.remove(str(pk))
            likeList = 'x'.join(likeList)
            likeList = likeList + 'x'   
            user.likeList = likeList
            user.save()        
            post.likes -= 1
            post.save()
        else:
            likeList.append(str(pk))
            likeList = 'x'.join(likeList)
            likeList = likeList + 'x'   
            user.likeList = likeList
            user.save()
            post.likes += 1
            post.save()

        return redirect('home')
