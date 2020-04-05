from django.shortcuts import render,redirect
from .models import stock
from .forms import StockForm
from django.contrib import messages
# Create your views here.
def home(request):

    #pk_d5626d51a17a452da5ad78b3d0e51d04
    import requests
    import json
    if request.method=="POST":
        input_s=request.POST['input_stock']
        URL="https://sandbox.iexapis.com/stable/stock/"+input_s+"/quote?token="
        #print(URL)
        api_requests=requests.get(url=URL)
        try:
            api=json.loads(api_requests.content)
        except Exception as e:
            api="Error"
        return render(request,'index.html',{'api':api})
    else:
        return render(request,'index.html',{'Error':"Try something Else"})

    
def about(request):
    return render(request,'about.html',{})
def add_stock(request):
    import requests
    import json
    if request.method=="POST":
        form=StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock added succesfully"))
            return redirect('add_stock')
            

        #input_s=request.POST['input_stock']
    else:
        data=stock.objects.all()
        output=[]
        for data_item in data:
            URL="https://sandbox.iexapis.com/stable/stock/"+str(data_item)+"/quote?token="
        #print(URL)
            api_requests=requests.get(url=URL)
            try:
                api=json.loads(api_requests.content)
                output.append(api)
            except Exception as e:
                api="Error"
            

        return render(request,'add_stock.html',{'data':data,'Output':output})
def delete(request,stock_id):
    item=stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("Item deleted"))
    return redirect(delete_stock)
def delete_stock(request):
    data=stock.objects.all()
    return render(request,'delete.html',{"data":data})
    