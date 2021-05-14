from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from order.data_scraper import Scraper

class Command(BaseCommand):

    help = 'Populates or updates database with new products'

    def handle(self, *args, **kwargs):
        headers = settings.HEADERS
        url = settings.SCRAPE_URL
        dataframe = Scraper(url, headers)
        dataframe.run()
