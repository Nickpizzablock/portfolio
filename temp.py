from bs4 import BeautifulSoup

# Sample HTML
html_content = """
<html><head><title>Page Title</title></head><body><h1>My Heading</h1><p>My paragraph.</p></body></html>
"""

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

def custom_prettify(tag, indent=0):
    """
    Custom prettify function to format HTML with specific newline rules.
    """
    result = []
    # Define tags that should have a newline
    tags_with_newline = {'title'}

    if tag.name in tags_with_newline:
        result.append('\n' + ' ' * indent)
    
    result.append(f'<{tag.name}>')

    for child in tag.children:
        if isinstance(child, str):
            result.append(child)
        else:
            result.extend(custom_prettify(child, indent + 2))
    
    result.append(f'</{tag.name}>')
    
    if tag.name in tags_with_newline:
        result.append('\n' + ' ' * (indent - 2))
    
    return result

# Create a new BeautifulSoup object from the formatted content
formatted_html = ''.join(custom_prettify(soup.html))
print(formatted_html)
