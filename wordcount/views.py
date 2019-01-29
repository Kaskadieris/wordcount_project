from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html',{})

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddictionary ={}

	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#add to dictionary
			worddictionary[word] = 1


	context = {
	'fulltext' : fulltext,
	'count': len(wordlist),
	'worddictionary': sorted(worddictionary.items(), key=operator.itemgetter(1), reverse =True),

	}


	return render(request,'count.html',context)

def about(request):
	return render(request,'about.html',{})