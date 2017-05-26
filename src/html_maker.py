
def html_helper(file_name='', parameters=[]):
    """
    html helper generates the html for directory listing
    """
    html_file = open(file_name, "w")
    print(parameters)
    html_file.write(html_maker(parameters))
    html_file.close()
    return html_file


def html_maker(parameters):
    """
    html_maker generates the html for directory listing
    """
    file1, file2, file3 = parameters
    return """
<html>
    <head>
        <title>directory</title>
    </head>
    <body>
        <h1>directory</h1>
        <ul>
            <li><a href="{}">{}</a></li>
            <li><a href="{}">{}</a></li>
            <li><a href="{}">{}</a></li>
        </ul>
        <p>Some text.</p>

    </body>
</html>
""".format(file1, file1, file2, file2, file3, file3)


if __name__ == "__main__":
    html_helper()
