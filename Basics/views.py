from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        result=int(num1+num2)
        return render(request,'Basics/Sum.html',{'Sum':result,'num1':num1,'num2':num2})
    else:
        return render(request,'Basics/Sum.html')
def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        btn=(request.POST.get("btn"))
        if btn=="Add":
           result=num1+num2
        elif btn=="Subtract":
           result=num1-num2
        elif btn=="Product":
            result=num1*num2
        elif btn=="Divide":
            result=num1/num2
        return render(request,'Basics/Calculator.html',{"result":result,"num1":num1,"num2":num2})
    else:
       return render(request,'Basics/Calculator.html')
def LargestSmallest(request):
    if request.method == "POST":
        num1 = int(request.POST.get("txt_num1"))
        num2 = int(request.POST.get("txt_num2"))
        num3 = int(request.POST.get("txt_num3"))
        largest = num1
        if num2 > largest:
            largest = num2
        if num3 > largest:
            largest = num3
        smallest = num1
        if num2 < smallest:
            smallest = num2
        if num3 < smallest:
            smallest = num3

        return render(request, 'Basics/LargestSmallest.html', {
            'largest': largest, 
            'smallest': smallest, 
            'num1': num1, 
            'num2': num2, 
            'num3': num3
        })
    else:
        return render(request, 'Basics/LargestSmallest.html')