from django.shortcuts import render

def cart_detail_view(request):
    return render(request, 'cart/cart.html')

def test(request):
    response = request.method
    response2 = request.path
    id = request.GET.get('id', 'id not selected')
    response3 = request.get_full_path()
    response4 = request.build_absolute_uri()
    response5 = request.META['REMOTE_ADDR']
    response6 = request.META.get('HTTP_USER_AGENT')
    return render(request, 'cart/test.html', context={
        'data': {
            'request.method':[response,],
            'request.path':[response2],
            'request.get_full_path()':[response3],
            'request.build_absolute_uri()':[response4],
            'request.META["REMOTE_ADDR"]':[response5],
            ' request.META.get("HTTP_USER_AGENT")':[response6],
            
        }
    })