def includeme(config):
    """ This function adds routes to Pyramid's Configurator """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('input_entry', '/input_entry')
    config.add_route('single_entry', '/single_entry')
    config.add_route('edit_entry', '/edit_entry')
