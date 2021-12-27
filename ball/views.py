from django.shortcuts import render,redirect

def home(request):
	return render(request,'ball/index.html')

def game(request):
	p1 = request.POST.get('p1',False)
	p2 = request.POST.get('p2',False)	
	s = request.POST.get('score',False)
	return render(request,'ball/game.html',{'player1':p1,'player2':p2,'score':s})

def gameover1(request):
	return render(request,'ball/gameover1.html')

def gameover2(request):
	return render(request,'ball/gameover2.html')
