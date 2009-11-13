from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from satchmo_store.shop.models import Order

@staff_member_required
def admin_order_export(request, status=None, template="admin/order_export/orders.csv", mimetype="text/csv"):
    """Admin authenticated order export.
    """
    
    if status:
        orders = Order.objects.filter(status=status).order_by('id')
    else:
        orders = Order.objects.all().order_by('id')
    
    return render_to_response(
        template, 
        {
            'orders' : orders,
        },
        mimetype=mimetype)