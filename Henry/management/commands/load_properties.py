import csv
from django.core.management.base import BaseCommand
from Henry.models import Property
import re


class Command(BaseCommand):
    help = 'Load properties from CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = "C:\\Users\\Sravan Kumar\\Mexico\\Website_mexico\\lamudi_properties.csv"  # Update this path if needed

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price_text = row.get('price', '0')
                cleaned_price = re.sub(r'[^\d]', '', price_text)
                row['price'] = int(cleaned_price) if cleaned_price else 0

                # Handle empty numeric fields with default values
                row['bedroom'] = int(row.get('bedroom', 0)) if row.get('bedroom') else 0
                row['bathroom'] = int(row.get('bathroom', 0)) if row.get('bathroom') else 0
                row['built'] = row.get('built', 'Unknown')  # Handle any other fields as needed

                Property.objects.create(
                    title=row['title'],
                    location=row['location'],
                    price=row['price'],
                    bedrooms=int(row['bedroom']) if row['bedroom'] else None,
                    bathrooms=int(row['bathroom']) if row['bathroom'] else None,
                    area=row['built'],
                    site_url=row['url'],
                    image_url=row['images']  # Store as-is, or parse if needed
                )

        self.stdout.write(self.style.SUCCESS('Properties loaded successfully.'))
