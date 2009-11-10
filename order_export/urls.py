"""
Urls for order export, note that this does not have to get added manually to the urls, it will be added automatically by satchmo core if this app is installed.
"""
from django.conf.urls.defaults import *
import logging
log = logging.getLogger('order_export.urls')

urlpatterns = patterns('order_export.views',
    (r'^admin/order_export/new_orders.csv$', 'admin_order_export', {'status':'New', 'template':"admin/order_export/orders.csv"}, 'admin_new_order_export'),
)

def add_export_urls(sender, patterns=(), **kwargs):
    log.debug("Adding order_export urls")
    patterns += urlpatterns
