from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from lms.models import Member
from lms.utils import del_values_by_key, validate_book_data

from lms.forms import MemberForm


@login_required(login_url='login')
def member_list(req):
    members = [
        {
            "id": 1,
            "name": "Shisihr",
            "e_mail": "shishir@example.com",
            "bio": "I Am The Boss"
        },
        {
            "id":2,
            "name":"Taukir",
            "e_mail": "taukir@example.com",
            "bio":"I Am Donkey"
        }
    ]


    context = {

            'members': members
    }
    return render (req,"lms/member_list.html",context=context)



#
# def new_member(request):
#     template = 'lms/new_member.html'
#     context = {
#
#     }
#
#     return render(request, template, context=context)
#


class NewMemberView(LoginRequiredMixin, View):
    login_url = 'login'
    template = 'lms/new_member.html'

    def get(self, request):
        name = request.session.get('name', '')
        email = request.session.get('email', '')
        bio = request.session.get('bio', '')

        member_form = MemberForm(initial={
            'name': name,
            'email': email,
            'bio': bio
        })
        member_form.is_valid()
        return render(request, self.template, context={'member_form': member_form})

    def post(self, request):
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            name = member_form.cleaned_data['name']
            email = member_form.cleaned_data.get('email', None)
            bio = member_form.cleaned_data.get('bio', None)

            member = Member()
            member.name = name
            if email:
                member.email = email
            if bio:
                member.bio = bio
            member.save()
            messages.add_message(request, messages.INFO, f"Created member with id {member.id}")
            del_values_by_key(request.session, 'name', 'email', 'bio')
        else:
            name = request.POST.get('name')
            email = request.POST.get('email', None)
            bio = request.POST.get('bio', None)
            request.session['name'] = name
            request.session['email'] = email
            request.session['bio'] = bio
            messages.add_message(request, messages.ERROR, f"Member could not be created")

        return redirect('new-member')
