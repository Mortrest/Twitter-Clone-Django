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