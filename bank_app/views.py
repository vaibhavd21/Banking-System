from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer



allcust = Customer.objects.all()
allids = []
for i in allcust:
    allids.append(int(i.id))
# Create your views here.
def home(request):
    return render(request,'index.html')

def customers(request):
    cust=Customer.objects.all()
    #print(cust)
    return render(request,'customer.html',{'custs':cust})

def custinfo(request,id):
    global allids
    cust=Customer.objects.filter(id=id)   #returns iterator queryset
    cust1 = Customer.objects.get(id = id)  #returns single object
    if request.method == 'GET':
        return render(request,'custinfo.html',{'customer':cust,'cur_cust_id':id})  
    #print(data)
    if request.method == 'POST':
        account_num = request.POST['AccountNum']
        Rec_name = request.POST['RName']
        amount = request.POST['Amount']

        #print(type(account_num)) str
        #print(Rec_name)
        #print(type(amount))   #str
        #print(type(cust1.balance))   #int

        #account_num_validation = Customer.objects.filter(id = id)
        #print(account_num_validation, " View Customer id ")

        #print(allids)
        if int(account_num) not in allids:
            #print("not in db")
            return render(request,'custinfo.html',{'customer':cust,'invalid_account_num':1,'cur_cust_id':id})

        if int(amount) <= 0: 
            return render(request,'custinfo.html',{'customer':cust,'invamnt':1,'cur_cust_id':id})

        temp = cust1.balance - int(amount)
        if temp < 0:
            return render(request,'custinfo.html',{'customer':cust,'lessthanzero':1,'cur_cust_id':id})


        cust1.balance = cust1.balance - int(amount)
        cust1.save()
        rec_obj = Customer.objects.get(id = account_num)
        #print(rec_obj, "Receriver id")
        if rec_obj:
            rec_obj.balance = rec_obj.balance + int(amount)
            rec_obj.save()
            return render(request,'custinfo.html',{'customer':cust,'successful':1,'cur_cust_id':id})
            
            
            
      
