#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import datetime
import time
import sys
import os
import re
from unicodedata import normalize

AUTHOR = 'xr09'
TODAY = datetime.date.today().isoformat()
NOW = time.strftime('%H:%M')
DEFAULT_CATEGORY = 'dev'

# slugify from http://flask.pocoo.org/snippets/5/
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


# you need at least one letter to make a valid post title
if len(sys.argv) < 2:
    print('Too few arguments')
    sys.exit(1)


title = u' '.join(sys.argv[1:])
slug = slugify(title.lower())

if os.path.exists(slug+'.rst'):
    print('A file with the same title already exists. Aborting!')
    sys.exit(1)

SUBHEADER = '#' * len(title)

TEMPLATE = """{title}
{SUBHEADER}
:date: {TODAY} {NOW}
:category: {DEFAULT_CATEGORY}
:tags: 
:author: {AUTHOR}
:excerpt:
""".format(**locals())
 

with open(slug+'.rst', 'w') as f:
    f.write(TEMPLATE)

# go blog, speak your mind with pelican    
os.system('xdg-open '+slug+'.rst')
