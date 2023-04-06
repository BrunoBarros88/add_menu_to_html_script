import os

#Send the file paths to add bootstrap and jquery links, so as the java script to the html
html_dir = r"C:\exemple\example\example"
bootstrap_path = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
jquery_path = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"
javascript_path = r"C:\your\path\to\menu.js"

# Define the HTML snippets
bootstrap_link = '<link rel="stylesheet" type="text/css" href="{}">'.format(bootstrap_path)
jquery_link = '<script type="text/javascript" src="{}"></script>'.format(jquery_path)
javascript_script = '<script type="text/javascript" src="{}"></script>'.format(javascript_path)

def add_links_and_scripts(html_file):
    with open(html_file, "r+", encoding="utf-8") as f:
        file_contents = f.readlines()

        # Position you want to insert 
        title_index = -1
        for i, line in enumerate(file_contents):
            if "</title>" in line:
                title_index = i
                break

        
        if title_index >= 0:
            file_contents.insert(title_index + 1, bootstrap_link + "\n")
            file_contents.insert(title_index + 2, jquery_link + "\n")

        
        footer_index = -1
        for i, line in enumerate(file_contents):
            if "</footer>" in line:
                footer_index = i
                break

        
        if footer_index >= 0:
            file_contents.insert(footer_index, javascript_script + "\n")

        
        f.seek(0)
        f.writelines(file_contents)
        f.truncate()

# Looping through all HTML files in the directory 
for filename in os.listdir(html_dir):
    if filename.endswith(".html"):
        html_file = os.path.join(html_dir, filename)
        add_links_and_scripts(html_file)
