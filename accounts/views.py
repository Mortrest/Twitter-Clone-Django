from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator
from .models import *
import re


#homePage View
def homePage(request):
    profile = Profile.objects.get(id=request.user.id)
    post = profile.post_set.order_by('-dateCreated')[:1000]
    paginator = Paginator(post,3)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    num_pages = paginator.num_pages 

    context = {
        'profile':profile,
        'post':post,
        'n':range(1,paginator.num_pages+1),
        'num_pages': num_pages,
        'page_number': page_number,
    }
    return render(request,'accounts/index.html',context)



def profilePage(request, pk):
    profile = Profile.objects.get(id=pk)
    user1 = Profile.objects.get(id=request.user.id)
    pattern = re.compile('[A-Za-z0-9]+@')
    followList = pattern.findall(user1.followList)
    followList = [i.rstrip('@') for i in followList]

    context = {
        'profile':profile,
        'followList':followList
    }
    return render(request,'accounts/profilePage.html',context)




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
    user1 = Profile.objects.get(id=request.user.id)
    pattern = re.compile('[A-Za-z0-9]+@')
    followList = pattern.findall(user1.followList)
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
            # d = target.post_set.all()
            # for i in d:
            #     user1.delete()  
            user1.followList = followList
            d = target.post_set.all()
            for i in d:
                i.user.remove(user1)  


            user1.followings -= 1
            user1.save()        
            target.followers -= 1
            target.save()
        else:
            followList.append(target.username)
            followList = '@'.join(followList)
            followList = followList + '@' 
            d = target.post_set.all()
            for i in d:
                i.user.add(user1)  


            user1.followList = followList
            user1.followings += 1
            user1.save()        
            target.followers += 1
            target.save()

        return redirect('profile',pk=pk)



#Like Function 
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
            post.likesCount -= 1
            post.save()
        else:
            likeList.append(str(pk))
            likeList = 'x'.join(likeList)
            likeList = likeList + 'x'   
            user.likeList = likeList
            user.save()
            post.likesCount += 1
            post.save()

        return redirect('home')


#Like Function (UnTest)
def likeFunctionFollow(request, pk):
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
            post.likesCount -= 1
            post.save()
        else:
            likeList.append(str(pk))
            likeList = 'x'.join(likeList)
            likeList = likeList + 'x'   
            user.likeList = likeList
            user.save()
            post.likesCount += 1
            post.save()

        return redirect('profile', kwargs=pk)