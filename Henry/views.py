from ast import literal_eval
from datetime import date

from django.core.serializers import serialize
from django.utils.safestring import mark_safe

from .models import Property
from django.shortcuts import render


# Create your views here.
def home(request):
    featured_properties = Property.objects.all()[:8]  # Get the first 8 properties or however many you want to display

    # Update each property's image_url to only contain the first URL
    for featured_property in featured_properties:
        try:
            # Use literal_eval to convert the string representation of the list into an actual list
            image_list = literal_eval(featured_property.image_url)
            # Assign only the first URL (if it exists)
            featured_property.cover_image_url = image_list[0] if image_list else None
        except (ValueError, SyntaxError):
            featured_property.cover_image_url = None  # Handle cases where image_url format is unexpected

    # Pass the updated queryset as context
    context = {'featured_properties': featured_properties}
    return render(request, 'Henry/index.html', context)


def featured_properties(request):
    properties = Property.objects.all()

    # Update each property's image_url to only contain the first URL
    for property in properties:
        try:
            # Convert the string representation of the list into an actual list
            image_list = literal_eval(property.image_url)
            property.cover_image_url = image_list[0] if image_list else None
        except (ValueError, SyntaxError):
            property.cover_image_url = None

    # Serialize the queryset to JSON format
    properties_json = mark_safe(serialize('json', properties))

    context = {
        'properties': properties,
        'properties_json': properties_json  # Pass serialized JSON data
    }
    return render(request, 'Henry/featured_properties.html', context)


def blog(request):
    posts = [
        {
            'id': 1,
            'title': 'Exploring Real Estate Investment Opportunities',
            'author': 'John Doe',
            'date': date(2023, 11, 1),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Discover the latest insights into the real estate investment market and tips for maximizing returns.',
        },
        {
            'id': 2,
            'title': 'Tips for First-Time Homebuyers',
            'author': 'Jane Smith',
            'date': date(2023, 10, 15),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Learn essential tips to help you navigate the home buying process smoothly and make informed decisions.',
        },
        {
            'id': 3,
            'title': 'Tips for First-Time Homebuyers',
            'author': 'Jane Smith',
            'date': date(2023, 10, 15),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Learn essential tips to help you navigate the home buying process smoothly and make informed decisions.',
        },
        {
            'id': 4,
            'title': 'Tips for First-Time Homebuyers',
            'author': 'Jane Smith',
            'date': date(2023, 10, 15),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Learn essential tips to help you navigate the home buying process smoothly and make informed decisions.',
        },
        {
            'id': 5,
            'title': 'Tips for First-Time Homebuyers',
            'author': 'Jane Smith',
            'date': date(2023, 10, 15),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Learn essential tips to help you navigate the home buying process smoothly and make informed decisions.',
        },
        {
            'id': 6,
            'title': 'Tips for First-Time Homebuyers',
            'author': 'Jane Smith',
            'date': date(2023, 10, 15),
            'image_url': 'https://via.placeholder.com/400x300',
            'excerpt': 'Learn essential tips to help you navigate the home buying process smoothly and make informed decisions.',
        },
        # Add more blog posts here
    ]

    context = {'posts': posts}
    return render(request, 'Henry/blog.html', context)


def blog_page(request):
    return render(request, 'Henry/blog_page.html')
