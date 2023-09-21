from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from .forms import ResumeForm
from .models import Candidate
from django.views import View



class HomeView(View):
    # method for rendering empty form by creating empty form object from ResumeForm form class
    def get(self,request):
        form = ResumeForm()
        return render(request, 'resumeapp/index.html', {'form': form})
    
    # method for capturing data from UI form and saving in database
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ResumeForm()
            return HttpResponseRedirect('/show')

#Fetching all the objects from database        
class ShowView(View):
    def get(self, request):
            form = Candidate.objects.all()
            return render(request, 'resumeapp/show.html',{'form': form})

#fetching single object based on id
class CandidateView(View):
    def get(self, request,id):
        candidate_data = Candidate.objects.get(id=id)
        return render(request, 'resumeapp/candidate.html',{'candidate': candidate_data})