import json
from dashboard_app.models import Dashboard_data
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):
    help = 'Import JSON Files'
    def handle(self, *args, **kwargs):
        with open(r'C:\Users\rachi\PycharmProjects\blackcofferassignment\dashboard_project\jsondata (1).json', 'r', encoding='utf8') as file:
            data=json.load(file)
            
            for item in data:
                 start_year = item.get('start_year')
                 start_year_value = int(start_year) if start_year and isinstance(start_year, (int, float, str)) else None

                 end_year = item.get('end_year')
                 end_year_value = int(end_year) if end_year and isinstance(end_year, (int, float, str)) else None

                 intensity_str = item.get('intensity')
                 intensity_value = int(intensity_str) if intensity_str and isinstance(intensity_str, (int, float, str)) else None

                 added_str = item.get('added')
                 added_date = datetime.strptime(added_str, '%B, %d %Y %H:%M:%S') if added_str else None       
 
                 published_str = item.get('published')
                 try:
                    published_date = datetime.strptime(published_str, '%B, %d %Y %H:%M:%S') if published_str else None
                 except (TypeError, ValueError):
                    published_date = None

                 relevance_str = item.get('relevance')
                 relevance_value = int(relevance_str) if relevance_str and isinstance(relevance_str, (int, float, str)) else None
                 
                 likelihood_str = item.get('likelihood')
                 likelihood_value = int(likelihood_str) if likelihood_str and isinstance(likelihood_str, (int, float, str)) else None
                 
                 Dashboard_data.objects.create(
                    end_year=end_year_value,
                    intensity=intensity_value,
                    sector=item.get('sector'),
                    topic=item.get('topic'),
                    insight=item.get('insight'),
                    url=item.get('url'),
                    region=item.get('region'),
                    start_year=start_year_value,
                    impact=item.get('impact'),
                    added=added_date,
                    published=published_date,
                    country=item.get('country'),
                    relevance=relevance_value,
                    pestle=item.get('pestle'),
                    source=item.get('source'),
                    title=item.get('title'),
                    likelihood=likelihood_value

                )

        self.stdout.write(self.style.SUCCESS('DONE'))        

