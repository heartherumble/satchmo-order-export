from django.conf.urls.defaults import *

urlpatterns = patterns('order_export.views',
    (r'^new_orders.csv$', 'admin_order_export', {'status':'New'}, 'admin_new_order_export'),
)