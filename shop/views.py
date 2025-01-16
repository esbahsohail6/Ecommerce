from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Contact,Order,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    allprods = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods':allprods}
    return render(request, 'shop/index.html', params)

def safe_lower(attribute):
        try:
            return str(attribute).lower()
        except Exception as e:
            print(f"Error converting attribute to string: {e}")
            return ""

def searchMatch(query,item):
    if (query in safe_lower(item.description) or
        query in safe_lower(item.product_name) or
        query in safe_lower(item.product_category)):
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(product_category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods':allprods, "msg": ""}
    if len(allprods) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    contact= False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, description=desc)
        contact.save()
        contact = True
    return render(request, 'shop/contact.html', {'contact': contact})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')
    # if request.method=="POST":
    #     orderId = request.POST.get('orderId', '')
    #     email = request.POST.get('email', '')
    #     try:
    #         order = Order.objects.filter(order_id=orderId, email=email)
    #         if len(order)>0:
    #             update = OrderUpdate.objects.filter(order_id=orderId)
    #             updates = []
    #             for item in update:
    #                 updates.append({'text': item.update_desc, 'time': item.timestamp})
    #                 response = json.dumps([updates,order[0].items_json],default=str)
    #                 # response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
    #             return HttpResponse(response)
    #         else:
    #             return HttpResponse('{}')
    #     except Exception:
    #         return HttpResponse('{}')
    # return render(request, 'shop/tracker.html')




def productview(request,prodid):
    product = Product.objects.filter(id=prodid)
    # print(product)
    return render(request,'shop/productview.html',{'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        print(name)
        order = Order(items_json=items_json,name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        # update = OrderUpdate(oder_id=order.order_id, update_desc="The order has been placed")
        # update.save()
        ord = True
        id = order.order_id
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        return render(request, 'shop/checkout.html', {'ord':ord, 'id': id})
    return render(request,'shop/checkout.html')



def feedback(request):
    return HttpResponse("feedback")



def cashback(request):
    return HttpResponse("cashback")


