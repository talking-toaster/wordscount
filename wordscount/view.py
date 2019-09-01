from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['user_text']
    user_count = len(user_text)
    user_word = {}
    for word in user_text:
        if word not in user_word:
            user_word[word] = 1
        else:
            user_word[word] += 1
    user_word = sorted(user_word.items(), key=lambda w: w[1], reverse=True)
    return render(request, 'count.html',
                  {'text': user_text, 'count': user_count,
                   'words': user_word})


def about(request):
    return render(request, 'about.html')

def call(request):
    return render(request,'call.html')
