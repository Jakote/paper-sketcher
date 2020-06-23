import subprocess, os, io
import reportlab
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import RegisterForm, ProfileForm,CSProposalForm, CSResearchpaperForm, CSThesisForm, ISThesisForm, ISProposalForm, ISResearchpaperForm
from .models import Profile, CS_Research_Paper,CS_Proposal,CS_Thesis,IS_Thesis,IS_Proposal,IS_Research_Paper
from django.http import FileResponse, Http404
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('home')
            
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('index')
        
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            request.session['username'] = username
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'signUp.html', {'form': form})

def sketch(request):
    user = User.objects.get(username=request.user.username)
    user_guery_set = Profile.objects.filter(user=user)
    form = ProfileForm()
    if user_guery_set is not None:
        for logged_user in user_guery_set:
            if logged_user.type_of_paper == 'Proposal Paper' and logged_user.domain_of_Knowledge =='Computer Science':
                form = CSProposalForm()
                if request.method == 'POST':
                    author = CS_Proposal(author=user)
                    form = CSProposalForm(request.POST, instance=author)    
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})

            if logged_user.type_of_paper == 'Research Paper' and logged_user.domain_of_Knowledge =='Computer Science':
                form =  CSResearchpaperForm()
                if request.method == 'POST':
                    author = CS_Research_Paper(author=user)
                    form = CSResearchpaperForm(request.POST, instance=author)    
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})

            if logged_user.type_of_paper == 'Thesis Paper' and logged_user.domain_of_Knowledge =='Computer Science':
                form =  CSThesisForm()
                if request.method == 'POST':
                    author = CS_Thesis(author=user)
                    form = CSThesisForm(request.POST, instance=author)    
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})

            if logged_user.type_of_paper == 'Proposal Paper' and logged_user.domain_of_Knowledge =='Information Systems':
                form = ISProposalForm()
                if request.method == 'POST':
                    author = IS_Proposal(author=user)
                    form = ISProposalForm(request.POST, instance=author)    
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})

            if logged_user.type_of_paper == 'Research Paper' and logged_user.domain_of_Knowledge =='Information Systems':
                form = ISResearchpaperForm()
                if request.method == 'POST':
                    author = IS_Research_Paper(author=user)
                    form = ISResearchpaperForm(request.POST, instance=author)    
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})

            if logged_user.type_of_paper == 'Thesis Paper' and logged_user.domain_of_Knowledge =='Information Systems':
                form = ISThesisForm()
                if request.method == 'POST':
                    author = IS_Thesis(author=user)
                    form = ISThesisForm(request.POST, instance=author)
                    if form.is_valid(): 
                        form.save()
                        return redirect('home')
                return render(request, 'sketch.html', {'form': form})
    if request.method == 'POST':
        profile(request)
        return redirect('sketch')
    return render(request, 'sketch.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        user = User.objects.get(username=request.user.username)
        if form.is_valid(): 
            level = form.cleaned_data.get('level_of_knowledge')
            domain = form.cleaned_data.get('domain_of_Knowledge')
            paper_type = form.cleaned_data.get('type_of_paper')
            Profile.objects.filter(user=user).update(level_of_knowledge=level, domain_of_Knowledge=domain, type_of_paper=paper_type) 
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

def pdf_templates(request): 
    user = get_object_or_404(User, username=request.user.username)
    getPaper=""
    
    if CS_Research_Paper.objects.filter(author=user).exists():
        getPaper = CS_Research_Paper.objects.filter(author=user)
    if CS_Proposal.objects.filter(author=user).exists():
        getPaper = CS_Proposal.objects.filter(author=user)
    if CS_Thesis.objects.filter(author=user).exists():
        getPaper = CS_Thesis.objects.filter(author=user)
    if IS_Thesis.objects.filter(author=user).exists():
        getPaper = IS_Thesis.objects.filter(author=user)
    if IS_Proposal.objects.filter(author=user).exists():
        getPaper = IS_Proposal.objects.filter(author=user)
    if IS_Research_Paper.objects.filter(author=user).exists():
        getPaper = IS_Research_Paper.objects.filter(author=user) 


    if getPaper:     
        for content in getPaper:
            print(content)
            print(getPaper)
            with open('mytexfile.tex','r') as myfile:
                text = myfile.read()
                text_new = text.replace('username', content.author)
                # text_new1 = text.replace('Your text here2.', content.title)
                # text_new2 = text.replace('Your text here3.', content.introduction)
                # text_new3 = text.replace('Your text here4.', content.methodology)
                # text_new4 = text.replace('Your text here5.', content.conclusion)
                # text_new5 = text.replace('Your text here6.', content.references)
                #text_new = text.replace('English abstract here.', content.abstract)

                with open('mytexfile.tex','w') as output:
                    output.write(text_new)
                    # output.write(text_new1)
                    # output.write(text_new2)
                    # output.write(text_new3)
                    # output.write(text_new4)
                    # output.write(text_new5)
    
               
    #     with open('acknowledgements.tex','r') as myfile:
    #         text1 = myfile.read()
    #         text_new = text1.replace('Your text here', content.acknowledgement)

    #         with open('acknowledgements.tex','w') as output:
    #             output.write(text_new)

    #     with open('background.tex','r') as myfile:
    #         text2 = myfile.read()
    #         text_new= text2.replace('Your text here', content.background)

    #         with open('background.tex','w') as output:
    #             output.write(text_new2)
        
    #     # with open('conclusion.tex','r') as myfile:
    #     #     text3 = myfile.read()
    #     #     text_new = text3.replace('Your text here', content.conclusion)

    #     #     with open('conclusion.tex','w') as output:
    #     #         output.write(text_new)
        
    #     with open('cover.tex','r') as myfile:
    #         text4 = myfile.read()
    #         text_new = text4.replace('Your text here', content.author)

    #         with open('cover.tex','w') as output:
    #             output.write(text_new)

    #     # with open('introduction.tex','r') as myfile:
    #     #     text5 = myfile.read()
    #     #     text_new5 = text5.replace('Your text here.', content.introduction)

    #     #     with open('introduction.tex','w') as output:
    #     #         output.write(text_new5)
    
        x = subprocess.call('pdflatex mytexfile.tex', shell=True)
        #os.system('start mytexfile.pdf')
        try:
            return FileResponse(open('mytexfile.pdf', 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()
        # if x !=0:
        #     print('Exit-code not 0, check result!')
        # else: 
        #     os.system('start mytexfile.pdf')
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mytexfile.pdf"'
        return response
        return FileResponse(as_attachment=True, filename='mytexfile.pdf')
    return HttpResponse('<h2>Go back to \'Save Paper Content\' before sketching paper<\h2>')
    
  
def generate_paper(request):
    return FileResponse(as_attachment=True, filename='sometexfile.pdf')
    