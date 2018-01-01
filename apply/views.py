from django.core.context_processors import csrf
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template import RequestContext
from apply.models import Application, Status


def contact(request):
    context = {}
    template = "apply.html"
    return render(request, template, context)


def validate(request):
    context = {}
    template_success = "success.html"
    template_kickout = "apply.html"
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        ign = request.POST["ign"]
        position = request.POST["position"]
        details = request.POST["details"]
        status = Status.objects.get(name="New")
        application = Application(
            name=name, email=email, ign=ign, position=position, details=details, status=status)
        try:
            application.full_clean()
            application.save()
            users = User.objects.filter(is_superuser=True)
            emails = []
            for u in users:
                emails.append(u.email)
            send_mail("New Reach Network Application", "Someone has just sent in an application! Review it at reachnetwork.herokuapp.com/admin.",
                      "RN@reachnetwork.com", emails, fail_silently=False)
            context.update(csrf(request))
            return render(request, template_success, context, context_instance=RequestContext(request))
        except ValidationError as e:
            print (e)
            context = {"name": name, "email": email, "ign": ign, "position":
                       position, "details": details, "wasError": True, "error": e}
            context.update(csrf(request))
            return render(request, template_kickout, context, context_instance=RequestContext(request))
    else:
        return render(request, template_kickout, context)
