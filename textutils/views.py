#i have created this file- Ziyaul
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.htm')
	#return HttpResponse("Home")
	
def analyze(request):
	#get the text
	djtext=(request.POST.get('text','default'))
	removepunc=request.POST.get('removepunc','off')
	capslk=request.POST.get('capslk','off')
	newlineremover=request.POST.get('newlineremover','off')
	extraspaceremover=request.POST.get('extraspaceremover','off')
	charcount=request.POST.get('charcount','off')
	#analyzed=djtext
	if removepunc=="on":
		punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char
		params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
		djtext=analyzed
	#analyze the text
		#return render(request,'analyze.htm',params)
	if (capslk=="on"):
		analyzed=""
		for char in djtext:
			
			analyzed=analyzed+char.upper()
		params={'purpose':'Capitalized Text', 'analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,'analyze.htm',params)
	if(newlineremover=="on"):
		analyzed=""
		for char in djtext:
			if char !="\n":
				analyzed=analyzed+char
		params={'purpose':'Removed new lines','analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,'analyze.htm',params)		
	if(extraspaceremover=="on"):
		analyzed=""
		for index,char in enumerate(djtext):
			if not (djtext[index]==" " and djtext[index+1]==" "):
				analyzed=analyzed+char
		params={'purpose':'Removed Extra Spaces','analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,'analyze.htm',params)
	if(charcount=="on"):
		analyzed= 0
		for t in djtext:
 			if not(t == " "):
  				analyzed += 1


		params={'purpose':'Total characters entered=','analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,'analyze.htm',params)	
	if (removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and capslk!="on" and charcount!="on"):
		return HttpResponse("Please select any operation and try again")	

	return render(request,'analyze.htm',params)
#def capitalisefirst(request):
#	return HttpResponse('''capitalisefirst <hr> <br><a href="http://127.0.0.1:8000/">Homepage</a>''')
#def newlineremove(request):
#	return HttpResponse('''newlineremove <hr> <br><a href="http://127.0.0.1:8000/">Homepage</a>''')
#def charcount(request):
#	return HttpResponse('''charcount <hr> <br><a href="http://127.0.0.1:8000/">Homepage</a>''')	
#def spaceremover(request):
#	return HttpResponse('''spaceremover <hr> <br><a href="http://127.0.0.1:8000/">Homepage</a>''')