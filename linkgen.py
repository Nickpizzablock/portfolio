print("hello world")

import bs4
import csv

with open("quicklinks.html") as f:
    txt = f.read()
    soup = bs4.BeautifulSoup(txt)

# read the links from links.csv
links = {}
with open("links.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the first row
    for row in reader:
        if not all(cell.strip() == '' for cell in row):
            category = row[0].strip()
            name = row[1].strip()
            link = row[2].strip()
            if category not in links:
                links[category] = []
            links[category].append((name, link))

# print(links)
# exit()
# in quicklinks.html, within the nav element, add a new list of all the keys
nav = soup.find("nav")
ul = soup.new_tag("ul")
for category in links:
    li = soup.new_tag("li")
    a = soup.new_tag("a", href=f"#{category}")
    a.string = category
    li.append(a)
    ul.append(li)
nav.append(ul)

# for each key, make a section titled that key and make an unordered list of names
main = soup.find("main")
for category, entries in links.items():
    section = soup.new_tag("section")
    h2 = soup.new_tag("h2", id=category)
    h2.string = category
    section.append(h2)
    ul = soup.new_tag("ul")
    for name, link in entries:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=link)
        a.string = name
        li.append(a)
        ul.append(li)
    section.append(ul)
    main.append(section)

# write the modified HTML back to quicklinks.html
# with open("quicklinksmod.html", "w") as f:
#     f.write(str(soup))

with open("quicklinksmod.html", "w") as f:
    # f.write(str(soup.prettify()))
    f.write(str(soup))
    # f.write(str(soup.prettify().replace("</li>\n", "</li>").replace("</a>\n", "</a>")))

# parse quicklinksmod
with open("quicklinksmod.html", "r") as f:
    html = f.read()
    soup = bs4.BeautifulSoup(html)

# remove all the newlines
html = html.replace("\n", "")

# for each tag, determine if it should have a newline before it
tags_with_newline_before = ["head", "main", "body", "nav", "ul", "html", "header", "section", "footer"]
tags_same_line = ["li", "h1", "h2", "p", "title"]
# after head, body, nav, ul, make a new line and indent the appropriate amount
for tag in tags_with_newline_before:
    html = html.replace(f"<{tag}", f"\n<{tag}")
    # html = html.replace(f"<{tag}>", f"\n<{tag}>")

for tag in tags_same_line:
    html = html.replace(f"<{tag}", f"\n<{tag}")

# after closing tags like /head, /body, /nav, /ul, make a new line and indent the appropriate amount
closing_tags = [f"/{tag}" for tag in tags_with_newline_before]
for tag in closing_tags:
    html = html.replace(f"<{tag}>", f"\n<{tag}>")
    # remove blank lines from html
# idk why there is a space between body and header???
html = "\n".join(line for line in html.split("\n") if line.strip())

new_html = ""
# loop through each line in html

indent = 0
tags_indent = ["header", "head", "main", "body", "nav", "ul", "header", "section", "footer"]
for line in html.split("\n"):
    for tag in tags_indent:
        if f"<{tag}" in line:
            new_html += (indent * " ") + line + "\n"
            indent += 4
            break
    else:
        if any(f"</{tag}" in line for tag in tags_indent):
            indent -= 4
        new_html += (indent * " ") + line + "\n"

# save the modified HTML to quicklinksmod_indent.html
with open("quicklinksmod_indent.html", "w") as f:
    f.write(new_html)
    # f.write(html)
