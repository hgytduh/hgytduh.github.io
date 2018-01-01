from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from members.models import Member
from forums.models import Topic, Post, Reply
from forums.forms import PostForm, ReplyForm
from django.utils import timezone


def Home(request):
    topics = Topic.objects.all()
    context = {"topics": topics}
    return render_to_response("topics.html",
                              context,
                              context_instance=RequestContext(request))


def topic(request, topic_name):
    topic = Topic.objects.get(title=topic_name)
    posts = Post.objects.filter(topic=topic).order_by("-lastUpdated")
    context = {"topic": topic, "posts": posts}
    return render_to_response("topic.html",
                              context,
                              context_instance=RequestContext(request))


def post(request, topic_name, post_id):
    topic = Topic.objects.get(title=topic_name)
    post = Post.objects.get(id=post_id)
    replies = Reply.objects.filter(post=post).order_by("date")
    context = {"topic": topic, "post": post, "replies": replies}
    if request.method == "POST" and request.user.is_authenticated():
        user = Member.objects.get(user=request.user)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = Reply.objects.create(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
                post=post,
                date=timezone.now(),
                author=user)
            reply.save()
            post.lastUpdated = reply.date
            post.save()
            return HttpResponseRedirect("/forums/" + topic_name + "/" + str(post_id))
        else:
            context.update({"form": form})
            return render_to_response("post.html",
                                      context,
                                      context_instance=RequestContext(request))
    else:
        form = ReplyForm()
        context.update({"form": form})
        return render_to_response("post.html",
                                  context,
                                  context_instance=RequestContext(request))


def newpost(request, topic_name):
    topic = Topic.objects.get(title=topic_name)
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/forums/" + topic_name)
    user = Member.objects.get(user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
                topic=topic,
                author=user,
                date=timezone.now(),
                lastUpdated=timezone.now())
            post.save()
            return HttpResponseRedirect("/forums/" + topic_name + "/" + str(post.id))
        else:
            return render_to_response("newpost.html",
                                      {"form": form},
                                      context_instance=RequestContext(request))
    else:
        form = PostForm()
        context = {"form": form, "topic": topic}
        return render_to_response("newpost.html",
                                  context,
                                  context_instance=RequestContext(request))
