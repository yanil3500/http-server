import os


def html_helper(file_location='', file_name='', parameters=[]):  # pragmals: no cover
    """
    html helper generates the html for directory listing
    """
    html_file = open(os.path.join(file_location, file_name), "w")
    html_file.write(_html_maker(parameters))
    html_file.close()
    return html_file


def html_str_maker(parameters=[], f_path=''):  # pragma: no cover
    """
    generates a str representation of an html file
    """
    return _html_maker(str(f_path), parameters)


def _html_maker(f_path, parameters):  # pragma: no cover
    """
    html_maker generates the html a directory listing
    """
    print(f_path)
    if f_path.endswith('t'):
        f_path = f_path + '/'
    if f_path.endswith('s'):
        f_path = f_path + '/'
    html_str = """<!DOCTYPE html><html><body><h1>directory</h1><ul></ul></body></html>"""
    ul_begin_tag = html_str.index('<ul>')
    ul_end_tag = html_str.index('</ul>')
    list_items = []
    for value in parameters:
        list_items.append('<li><a href="{}{}">{}</a></li>'.format(f_path[3:], value, value))
    html_str = '{}{}{}'.format(html_str[:ul_begin_tag + 4], ''.join(list_items), html_str[ul_end_tag + 5:])
    return html_str
