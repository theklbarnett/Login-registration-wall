from django.shortcuts import render, redirect
from login.models import User
from .models import Message, Comment
from django.http import JsonResponse
#from datetime import datetime

def render_wall(request):
	if request.session['logged_on']:
		context = {
			'posts': Message.objects.all().order_by('-created_at')
		}
		return render(request, 'wall.html', context)
	else:
		return redirect('/')

def post_message(request):
	if request.method == 'POST':
		Message.objects.create(message=request.POST['new_message'], user=User.objects.get(id=request.session['user_id']))
	return redirect('/wall')

def post_comment(request):
	if request.method == 'POST':
		Comment.objects.create(comment=request.POST['new_comment'], user_id=request.session['user_id'], message_id=request.POST['message_id'])
	return redirect('/wall')

def delete_post(request):
	data = {}
	if request.GET.get('post_id', None) != None:
		post_id = request.GET.get('post_id', None)
	#time zone messing it up and not allowing the aware and unaware dates to be subtracted
	#if (datetime.utcnow() - Message.objects.get(id=post_id).created_at).seconds < 30 * 60:		
		Message.objects.get(id=post_id).delete()
		data['deleted'] = True
	elif request.GET.get('comment_id', None) != None:
		comment_id = request.GET.get('comment_id', None)
		Comment.objects.get(id=comment_id).delete()
		data['deleted'] = True
	return JsonResponse(data)