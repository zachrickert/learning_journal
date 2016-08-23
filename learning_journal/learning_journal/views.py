from pyramid.response import Response 
import os

HERE = os.path.dirname(__file__)


def home_page(request):
    imported_text = open(os.path.join(HERE + '/static/', 'index.html')).read()
    return Response(imported_text)


def view_entry(request):
    imported_text = open(os.path.join(HERE + '/static/', 'single_entry.html')).read()
    return Response(imported_text)


def input_entry(request):
    imported_text = open(os.path.join(HERE + '/static/', 'input_entry.html')).read()
    return Response(imported_text)


def edit_entry(request):
    imported_text = open(os.path.join(HERE + '/static/', 'edit_entry.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(home_page, route_name='home')
    config.add_view(view_entry, route_name='single_entry')
    config.add_view(input_entry, route_name='input_entry')
    config.add_view(edit_entry, route_name='edit_entry')
