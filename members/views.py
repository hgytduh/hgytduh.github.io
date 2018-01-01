from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from members.forms import RegistrationForm, LoginForm, NewPasswordForm
from members.models import Member
from forums.models import Reply, Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def SurvivorRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password"])
            user.save()
            member = Member(
                user=user, ign=form.cleaned_data["ign"], title="Player")
            member.save()
            return HttpResponseRedirect('/home')
        else:
            return render_to_response("register.html", {"form": form},
                                      context_instance=RequestContext(request))
    else:
        # user is not submitting the form, show them a registration form
        form = RegistrationForm()
        context = {"form": form}
        return render_to_response('register.html', context,
                                  context_instance=RequestContext(request))


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/home')
            else:
                return render_to_response("login.html", {"form": form, "error": "There is no member with that username and password..."}, context_instance=RequestContext(request))
        else:
            return render_to_response("login.html", {"form": form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {"form": form}
        return render_to_response("login.html", context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect("/home")


def Home(request):
    members = Member.objects.all()
    context = {"users": members}
    return render_to_response("members.html", context, context_instance=RequestContext(request))


def profile(request, username):
    user = User.objects.get(username=username)
    member = Member.objects.get(user=user)
    posts = Post.objects.filter(author=member).order_by("-date")
    replies = Reply.objects.filter(author=member).order_by("-date")
    context = {"member": member, "posts": posts,
               "replies": replies}
    if request.method == "POST":
        form = NewPasswordForm(request.POST)
        if not form.is_valid():
            context.update({"form": form})
            return render_to_response("profile.html", context, context_instance=RequestContext(request))
        password = form.cleaned_data["password"]
        if request.user.is_authenticated and request.user == user:
            user.set_password(password)
            user.save()
            return HttpResponseRedirect("/members/logout")
        else:
            return HttpResponseRedirect("/members/" + username)
    else:
        form = NewPasswordForm()
        context.update({"form": form})
        return render_to_response("profile.html", context, context_instance=RequestContext(request))
