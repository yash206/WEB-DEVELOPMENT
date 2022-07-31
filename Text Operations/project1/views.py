from django.http import HttpResponse
from django.shortcuts import render


def noinput(s):
    if s == '':
        return True
    else:
        return False


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'No Input Text Found !!')
    rp = request.POST.get('removepunc', 'off')
    cf = request.POST.get('capfirst', 'off')
    nlr = request.POST.get('newlineremove', 'off')
    sr = request.POST.get('spaceremove', 'off')
    cc = request.POST.get('charcount', 'off')
    if noinput(djtext):
        return HttpResponse("No Input Detected!!")
    if rp == 'on':
        str1 = ""
        for i in djtext:
            if (33 <= ord(i) <= 47) or (58 <= ord(i) <= 64) or (91 <= ord(i) <= 96) or (123 <= ord(i) <= 126):
                continue
            else:
                str1 = str1 + i
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': str1}
        djtext = str1
    if cf == 'on':
        lst = djtext.split(" ")
        for i in range(len(lst)):
            lst[i] = lst[i].capitalize()
        str2 = ' '.join(lst)
        params = {'purpose': 'Capitalize First', 'analyzed_text': str2}
        djtext = str2
    if nlr == 'on':
        str3 = ''
        for i in djtext:
            if i != '\n' and i != '\r':
                str3 = str3 + i
        params = {'purpose': 'Remove New Line', 'analyzed_text': str3}
        djtext = str3
    if sr == 'on':
        str4 = ''
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                str4 = str4 + char
        params = {'purpose': 'Remove Space', 'analyzed_text': str4}
        djtext = str4
    return render(request, 'analyze.html', params)

