from django.shortcuts import render

# Create your views here.
def home(req):
    context = {
    }
    return render(req, "lms/home.html", context=context)


def about(req):
    context = {
    }
    return render(req, "lms/about.html", context=context)

def book_list(req):
    books = [
        {
            'id': 1,
            'title': 'Speak',
            'author': 'Laurie Halse Anderson',
            'description': 'Speak up for yourself—we want to know what you have to say.'
        },
        {
            'id': 1,
            'title': 'The Hunger Games',
            'author': 'Suzanne Collins',
            'description': """
Could you survive on your own, in the wild, with everyone out to make sure you don't live to see the morning? 
In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV. Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she is forced to represent her district in the Games. But Katniss has been close to dead before - and survival, for her, is second nature. 
Without really meaning to, she becomes a contender. 
But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.
"""
        }
    ]

    context = {
        'books': books
    }
    return render(req, "lms/book_list.html", context=context)

