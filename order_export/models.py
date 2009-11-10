from signals_ahoy.signals import collect_urls
from urls import add_export_urls
import satchmo_store

collect_urls.connect(add_export_urls, sender=satchmo_store)