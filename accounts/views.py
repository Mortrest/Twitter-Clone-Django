from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import *
import re
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *



@login_required(login_url='login')
#homePage View
def homePage(request):
	profile = Profile.objects.get(id=request.user.id)
	profile_last = Profile.objects.order_by('-dateCreated')[:4]
	post = profile.post_set.order_by('-dateCreated')[:1000]
	paginator = Paginator(post,3)
	page_number = request.GET.get('page')
	post = paginator.get_page(page_number)
	num_pages = paginator.num_pages 

	user1 = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[0-9]+x')
	likeList = pattern.findall(user1.likeList)
	likeList = [i.rstrip('x') for i in likeList]
	d = []
	form = TweetForm2()
	for i in range(len(likeList)):
		d.append(int(likeList[i]))
	context = {
		'profile':profile,
		'profile_last':profile_last,
		'post':post,
		'n':range(1,paginator.num_pages+1),
		'num_pages': num_pages,
		'page_number': page_number,
		'likeList':d,
		'form':form

	}
	return render(request,'accounts/base.html',context)

def homeFake(request):
	profile = Profile.objects.get(id=request.user.id)
	profile_last = Profile.objects.order_by('-dateCreated')[:4]
	post = profile.post_set.order_by('-dateCreated')[:2]
	paginator = Paginator(post,3)
	page_number = request.GET.get('page')
	post = paginator.get_page(page_number)
	form = TweetForm2()
	num_pages = paginator.num_pages 

	user1 = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[0-9]+x')
	likeList = pattern.findall(user1.likeList)
	likeList = [i.rstrip('x') for i in likeList]
	d = []
	for i in range(len(likeList)):
		d.append(int(likeList[i]))
	context = {
		'profile':profile,
		'profile_last':profile_last,
		'post':post,
		'n':range(1,paginator.num_pages+1),
		'num_pages': num_pages,
		'page_number': page_number,
		'likeList':d,
		'form':form
	}
	return render(request,'accounts/landingPage.html',context)





@unauth_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account Was Created '+ username)
			return redirect ('login')
	context = {
		'form':form
	}
	return render(request, 'accounts/register.html',context)



@unauth_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or Password is wrong')
	context = {
	}
	return render(request, 'accounts/loginPage.html', context)


@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')		

@login_required(login_url='login')
def detailView(request, pk):
	post = Post.objects.get(id=pk)
	user = Profile.objects.get(id=request.user.id)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data.get('body')
			q = post.comment_set.create(body=a)
			q.author = user
			q.save()
	context = {
		'post':post,
		'form':form,

	}
	return render(request, 'accounts/detailPage.html', context)


@login_required(login_url='login')
def deleteComment(request, pk1, pk2):
	post = Post.objects.get(id=pk1)
	try:
		z = 0
	except:
		w = 0
	else:
		q = post.comment_set.get(id=pk2)
		q.delete()
	return redirect('detail', pk=post.pk)


@login_required(login_url='login')
def deleteTweet(request, pk):
	post = Post.objects.get(id=pk)
	user1 = Profile.objects.get(id=request.user.id)
	try:
		z = 0
	except:
		w = 0
	else:
		if post.author == user1:
			post.delete()
		else:
			post.user.remove(user1)
		return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def deleteTweetDetail(request, pk):
	post = Post.objects.get(id=pk)
	user1 = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[A-Za-z0-9]+@')
	followerList = pattern.findall(user1.followerList)
	followerList = [i.rstrip('@') for i in followerList]

	try:
		z = 0
	except:
		w = 0
	else:
		if post.author == user1:
			post.delete()
		else:
			post.user.remove(user1)
		return redirect('home')
		


@login_required(login_url='login')
def followingList(request, pk):
	target = Profile.objects.get(id=pk)
	user = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[A-Za-z0-9]+@')
	profile_last = Profile.objects.order_by('-dateCreated')[:4]
	followingList = pattern.findall(target.followingList)
	followingList = [i.rstrip('@') for i in followingList]
	user = Profile.objects.get(id=request.user.id)
	profile = Profile.objects.get(id=request.user.id)
	post = profile.post_set.order_by('-dateCreated')[:1000]
	followingList.remove('0')
	context = { 
		'profile':profile,
		'post':post,
		'list':followingList,
		'target':target,
		'profile_last':profile_last
	}
	return render(request, 'accounts/followingList.html',context)




@login_required(login_url='login')
def followerList(request, pk):
	target = Profile.objects.get(id=pk)
	user = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[A-Za-z0-9]+@')
	profile_last = Profile.objects.order_by('-dateCreated')[:4]
	followerList = pattern.findall(target.followerList)
	followerList = [i.rstrip('@') for i in followerList]
	user = Profile.objects.get(id=request.user.id)

	profile = Profile.objects.get(id=request.user.id)
	post = profile.post_set.order_by('-dateCreated')[:1000]
	followerList.remove('0')
	context = { 
		'profile':profile,
		'target':target,
		'post':post,
		'list':followerList,
		'target':target,
		'profile_last':profile_last,
	}
	return render(request, 'accounts/followerList1.html',context)



@login_required(login_url='login')
def profilePage(request, username):
	profile = Profile.objects.get(username=username)
	user1 = Profile.objects.get(id=request.user.id)
	profile_last = Profile.objects.order_by('-dateCreated')[:4]

	pattern = re.compile('[A-Za-z0-9]+@')
	followingList = pattern.findall(user1.followingList)
	followingList = [i.rstrip('@') for i in followingList]
	post = profile.post_set.order_by('-dateCreated')[:1000]
	paginator = Paginator(post,3)
	page_number = request.GET.get('page')
	post = paginator.get_page(page_number)
	num_pages = paginator.num_pages 

	user1 = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[0-9]+x')
	likeList = pattern.findall(user1.likeList)
	likeList = [i.rstrip('x') for i in likeList]
	d = []
	for i in range(len(likeList)):
		d.append(int(likeList[i]))
	context = {
		'profile':profile,
		'followList':followingList,
		'profile_last':profile_last,
		'post':post,
		'n':range(1,paginator.num_pages+1),
		'num_pages': num_pages,
		'page_number': page_number,
		'likeList':d
	}
	
	return render(request,'accounts/profilePage.html',context)


def tweetPage(request):
	user = Profile.objects.get(id=request.user.id)
	form = TweetForm()
	context = {
		'user':user,
		'form':form,
	}
	return render(request, 'accounts/tweet.html',context)


@login_required(login_url='login')
#Tweet Function (UnTest)
def addTweet(request):
	user1 = Profile.objects.get(id=request.user.id)

	form = TweetForm()
	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data.get('body')
			q = Post.objects.create(body=a)
			q.author = user1
			q.user.add(user1)
			q.save()
			pattern = re.compile('[A-Za-z0-9]+@')
			followerList = pattern.findall(user1.followerList)
			followerList = [i.rstrip('@') for i in followerList]

			for i in followerList:
				if i != '0':
					d = Profile.objects.get(username=i)
					q.user.add(d)
					q.save()

			return redirect('home')
		else:
			form = TweetForm()


@login_required(login_url='login')
#Follow Function (UnTest)
def followFunction(request, pk):
	target = Profile.objects.get(id=pk)
	user1 = Profile.objects.get(id=request.user.id)
	pattern = re.compile('[A-Za-z0-9]+@')
	followingList = pattern.findall(user1.followingList)
	followingList = [i.rstrip('@') for i in followingList]
	try:
		q = 1
	except:
		a = 1
	else:
		if target.username in followingList:
			followingList.remove(target.username)
			followingList = '@'.join(followingList)
			followingList = followingList + '@' 
			# d = target.post_set.all()
			# for i in d:
			#     user1.delete()  
			user1.followingList = followingList
			d = target.post_set.filter(author=target)
			for i in d:
				i.user.remove(user1)  
			pattern = re.compile('[A-Za-z0-9]+@')
			followerList = pattern.findall(user1.followerList)
			followerList = [i.rstrip('@') for i in followerList]
			followerList.remove(user1.username)
			followerList = '@'.join(followerList)
			followerList = followerList + '@' 

			user1.followings -= 1
			user1.save()        
			target.followers -= 1
			target.save()
		else:
			followingList.append(target.username)
			followingList = '@'.join(followingList)
			followingList = followingList + '@' 
			d = target.post_set.all()
			for i in d:
				i.user.add(user1)  
			pattern = re.compile('[A-Za-z0-9]+@')
			followerList = pattern.findall(user1.followerList)
			followerList = [i.rstrip('@') for i in followerList]
			followerList.append(user1.username)
			followerList = '@'.join(followerList)
			followerList = followerList + '@' 


			user1.followingList = followingList
			target.followerList = followerList
			user1.followings += 1
			user1.save()        
			target.followers += 1
			target.save()

		return redirect('profile',pk=pk)



@login_required(login_url='login')
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
		return redirect(request.META['HTTP_REFERER'])



@login_required(login_url='login')
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
		return redirect(request.META['HTTP_REFERER'])



@login_required(login_url='login')
def searchView(request):
	if request.method == 'POST':
		search = request.POST.get('search')
		print(search)
		results = Profile.objects.filter(username__contains=search)
		context = {
			'results':results
		}
		return render(request, 'accounts/searchResult.html', context)
