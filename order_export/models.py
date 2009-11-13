from signals_ahoy.signals import collect_urls
from urls import add_export_urls
from satchmo_store import shop

collect_urls.connect(add_export_urls, sender=shop)
