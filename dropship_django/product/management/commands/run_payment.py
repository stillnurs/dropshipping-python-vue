from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from order.auto_payment import Payment

class Command(BaseCommand):

    help = 'Orders the product from assigned website'

    def handle(self, *args, **kwargs):
        headers = settings.HEADERS
        url = settings.SCRAPE_URL
        dataframe = Payment(url, headers)
        dataframe.run()