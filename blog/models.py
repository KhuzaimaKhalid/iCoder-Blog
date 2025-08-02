from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib import messages
from ckeditor_uploader.fields import RichTextUploadingField

    
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    content = RichTextUploadingField()
    slug = models.CharField(max_length = 130)
    author = models.CharField(max_length = 50)
    views= models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return "Post by " + self.author + " - " + self.title
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    parent = models.ForeignKey('self', on_delete = models.CASCADE, null = True)
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username 
    
def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment = comment, user = user, post = post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno = parentSno)
            comment = BlogComment(comment = comment, user = user, post = post, parent = parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")  