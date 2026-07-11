from django.shortcuts import render, get_object_or_404, redirect
from textiles.models import TotalFloors, products, supervisor

def Product_list(request, id=0):
    floor = get_object_or_404(TotalFloors, id=id)
    product = products.objects.filter(floor=floor)
    is_supervisor = supervisor.objects.filter(user_name=request.user, floor=floor).exists()
    return render(request, "productslist.html", {
        'floor': floor,
        'product': product,
        'is_supervisor': is_supervisor
    })

def add_to_cart_view(request):
    floor_id = request.GET.get('floor_id')
    all_products = products.objects.all()

    if floor_id:
        floor = get_object_or_404(TotalFloors, id=floor_id)
        all_products = products.objects.filter(floor=floor)

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity_str = request.POST.get('quantity')
        product = get_object_or_404(products, id=product_id)

        try:
            quantity = int(quantity_str)
        except (ValueError, TypeError):
            quantity = 1

        price = int(product.price)
        total_price = price * quantity

        if 'cart_items' not in request.session:
            request.session['cart_items'] = []

        cart = request.session['cart_items']
        cart.append({
            'product_name': product.product_name,
            'price': price,
            'quantity': quantity,
            'total_price': total_price
        })
        request.session.modified = True
        return redirect('cart_success')

    return render(request, 'addtocart.html', {
        'available_products': all_products
    })

def cart_success_view(request):
    cart_items = request.session.get('cart_items', [])
    for item in cart_items:
        item['total_price']=float(item['price'])*int(item['quantity'])   #calculate total price

    return render(request, 'cart_success.html', {
        'cart_items': cart_items,
        'total_items': len(cart_items)
    })


def generate_bill_view(request):
    cart_items=request.session.get('cart_items',[])
    total_amount=sum(item['price'] * item['quantity'] for item in cart_items)

    return render(request,'bill.html', {
        'cart_items' : cart_items,
        'total_amount' : total_amount
    })