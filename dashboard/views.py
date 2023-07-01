from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()  # for staff
    products = Product.objects.all()  # for admin

    worker_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()

    if request.method == 'POST': 
        form = OrderForm(request.POST)  # for staff
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user
            product = order.product
            product.quantity -= order.order_quantity
            product.save()
            form.save()

            return redirect('dashboard-index')
    else:
        form = OrderForm()    
    context = {
        'orders': orders,  
        'form': form,
        'products': products,
        'worker_count': worker_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/index.html',context)


@login_required
def staff(request):
    workers= User.objects.all()
    worker_count = workers.count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()

    context={ 
        'workers': workers,
        'worker_count': worker_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/staff.html',context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    worker_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()
    context = {
        'workers' : workers,
        'worker_count': worker_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):   # for create and read

    items = Product.objects.all() # using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product') #using SQL
    product_count = items.count()
    worker_count= User.objects.all().count()
    order_count = Order.objects.all().count()

    if(request.method == 'POST'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'worker_count': worker_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/product.html',context)

@login_required
def product_delete(request, key):  # for deleting product
    item = Product.objects.get(id = key)

    if request.method == 'POST':
        item.delete()
        messages.warning(request, f'{item} has been deleted.')
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

@login_required
def product_update(request,key):  # for updating/editing the product details
    item = Product.objects.get(id = key)

    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name') #we remove all other data and are bothered about username
            messages.success(request, f'{name} has been updated.')
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form
    }
    return render(request,'dashboard/product_update.html',context)


@login_required
def order(request):
    orders = Order.objects.all().order_by('-date')
    order_count = orders.count()
    product_count = Product.objects.all().count()
    worker_count= User.objects.all().count()

    total_sale = sum(order.sale for order in orders)
    
    context={
        'orders':orders,
        'worker_count': worker_count,
        'product_count': product_count,
        'order_count': order_count,
        'total_sale': total_sale,
    }
    return render(request, 'dashboard/order.html', context)

