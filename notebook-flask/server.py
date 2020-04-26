import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# Ref for blog:
# http://john-b-yang.github.io/flask-website/
# https://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/
# https://pythonhosted.org/Flask-FlatPages/

# Configuration
# 1. Pages are loaded on request
# 2. File name extensions for pages is markdown.

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

# Update Freezer configs
FREEZER_DESTINATION = "../"
FREEZER_REMOVE_EXTRA_FILES = False
FREEZER_DESTINATION_IGNORE = [".git*", "CNAME", ".gitignore", "readme.md"]
FREEZER_RELATIVE_URLS = True

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    """Url route to index"""
    #pages = (p for p in pages if 'published' in p.meta)
    #pages = sorted(pages, reverse=True, key=lambda p: p.meta['published'])

    return render_template('index.html', pages=pages)

@app.route("/<path:path>/")
def page(path):
    """Url routing to flat pages, retrieves page path."""
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

# @app.route('/<path:path>')
# def catch_all(path):
#     """
#     <path:path> will return path after 8020/ as path.
#     % curl 127.0.0.1:5000/foo/bar
#     path arg will be = 'foo/bar'
#     """
#     return 'You want path: %s' % path

if __name__ == "__main__":
    #app.run(port=8020)
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8020)
