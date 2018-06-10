from django.shortcuts import render
from .models import Banner
from .models import Post
from .models import Comment
from .models import Tags
from .models import BlogCategory
from .models import FriendlyLink
from django.views.generic.base import View
from django.db.models import Q
# Create your views here.
def index(request):

    banner_list = Banner.objects.all()
    post_list = Post.objects.filter(is_recomment=True)

    post_list1 = Post.objects.order_by('pub_date')
    comment_list = Comment.objects.all()
    tage_list = Tags.objects.all()

    blogcategory_list = BlogCategory.objects.all()
    friendlylink_list = FriendlyLink.objects.all()

    ctx = {

        'banner_list': banner_list,
        'post_list': post_list,
        'post_list1': post_list1,
        'comment_list': comment_list,
        'tage_list':tage_list,
        'blogcategory_list':blogcategory_list,
        'friendlylink_list':friendlylink_list,
    }




    return render(request, 'index.html', ctx)





#搜索
class Search(View):
    def get(self,request):
        pass

    def post(self, request):

        kw = request.POST.get('keyword')

        post_list = Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw)|Q(tags__name__icontains=kw)|Q(user__username__icontains=kw))

        ctx1 ={
            'post_list':post_list

        }

        return render(request,'list.html',ctx1)


def list(request):

    post_list = Post.objects.all()

    ztc ={
        'post_list':post_list
        }

    return render(request,'list.html',ztc)



def bq(request,q):

    post_list = Post.objects.filter(tags=q)

    q ={
        'post_list':post_list
    }

    return render(request,'list.html',q)