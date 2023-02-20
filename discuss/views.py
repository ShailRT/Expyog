from django.shortcuts import render, redirect
from .models import Query, Comment
from core.models import Profile, UserDetail
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/login')
def create_question(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        tags = request.POST['tags']
        body = request.POST['body']
        category = request.POST['category']
        category = slugify(category)
        files = request.FILES.get('files[]')
        query = Query.objects.create(title=title, tags=tags, category=category, body=body, image=files, user=user)

        profile = Profile.objects.filter(user=user).first()
        profile.questions += 1
        
        profile.save()
        query.save()
        
        return redirect('/')
        
    
    context = {
        
    }
    return render(request, 'ask-question.html', context)

def detail_question(request, pk):
    query = Query.objects.filter(query_id=pk).first()
    if request.user != query.assigned_user and request.user.is_superuser==False and request.user != query.user:
        return redirect('/?category=&page=1')

    if request.method == "POST":
        user = request.user
        message = request.POST['message']

        comment = Comment.objects.create(user=user, message=message, query=query)
        profile = Profile.objects.filter(user=user).first()
        profile.answers += 1
        profile.save()
        comment.save()
        return redirect('detail-question', pk=pk)

    else:   
        comment = Comment.objects.filter(query=query)
        query_tag = query.tags.split(',')

        context = {
            'query': query,
            'tags': query_tag,
            'comments': comment,
            'user': request.user
        }
        
        return render(request, 'question-detail.html', context)

def upvote(request):
    comment_id = request.GET.get('comment-id')
    query_id = request.GET.get('query-id')
    comment = Comment.objects.filter(id=comment_id, up_vote=request.user).first()

    if comment==None:
        comment = Comment.objects.filter(id=comment_id).first()
        comment.up_vote.add(request.user)
        comment.save()
        return redirect('detail-question', pk=query_id)
    else:
        return redirect('detail-question', pk=query_id)


def downvote(request):
    comment_id = request.GET.get('comment-id')
    query_id = request.GET.get('query-id')
    comment = Comment.objects.filter(id=comment_id, down_vote=request.user).first()

    if comment==None:
        comment = Comment.objects.filter(id=comment_id).first()

        comment.down_vote.add(request.user)
        comment.save()
        return redirect('detail-question', pk=query_id)
    else:
        return redirect('detail-question', pk=query_id)




