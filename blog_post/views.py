from django.shortcuts import render
from blog_post.models import Post

# Create your views here.
#I've started from here.
def home(request):
	all_post = Post.objects.all()
	#for post in all_post:
		#print(post)

	return render(request, 'index.html',{
		'all_post_list':all_post
		#'name': "Md. Shorif Hossain",
		#'district': "Dhaka"
		})

def  post_list(request):
	post_list = Post.objects.all()
	return render(request,'post_list.html',{'post_list':post_list})

def single_post(request,post_id):
	post = Post.objects.get(pk=post_id)
	print(post)
	return render(request, 'single_post.html',{'post':post})