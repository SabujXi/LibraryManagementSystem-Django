from django.shortcuts import render
from django.views import View



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

class NewMemberView(View):
    template = 'lms/new_member.html'

    template = "lms/add_edit_book.html"

    def get(self, request, member_id=None):
        errors = request.session.get('errors', {})
        # build book_data dict
        if member_id is None:  # non existing book
            member_data = {
                'name': request.session.get('name', ''),
                'token_books': request.session.get('token_books', ''),
                'description': request.session.get('description', '')
            }
            # remove data from session
            # del_values_by_key(request.session, 'name', 'token_books', 'description', 'errors')

        else: # existing book
            _member = Member.objects.get(id=member_id)
            member_data = {
                'id': _member.id,
                'token_books': _member.token_books,
                'description': _book.description
            }

        context = {
            'member_data': member_data,
            'errors': errors
        }
        return render(request, self.template, context=context)

    def post(self, request, member_id=None):
        # determine if the request is for new book or editing existing book.
        member_id = request.POST.get('member_id', None)
        if not member_id:  # empty string, None
            member_id = None
        if member_id is not None:  # conversion
            member_id = int(member_id)

        # validate submitted data.
        # TODO: process the form, validate it, save into db and report to the user - on failure report error.
        name = request.POST.get('name')
        token_books = request.POST.get('token_books')
        description = request.POST.get('description')
        # TODO: validate - pure python validator
        errors = validate_book_data(request.POST)

        if errors:
            request.session['name'] = name
            request.session['description'] = description
            request.session['errors'] = errors
        else:
            if member_id is None:
                member = Member()
            else:
                member = Member.objects.get(id=member_id)

            member.name = name
            memmber.token_books = token_books
            book.description = description
            member.save()
            messages.add_message(request, messages.INFO, f"{ 'Created' if member_id is None else 'Updated'} successfully with id {member.id}, title {member.title}")
        return redirect('new-member', member_id=member_id)
