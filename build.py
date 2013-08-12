#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs
import datetime

import markdown
from jinja2 import Template

__version__ = '0.1'

text = codecs.open("index.md", mode="r", encoding="utf-8").read()
html = markdown.markdown(text, extensions=['attr_list', 'headerid(forceid=False)'])

template = Template(codecs.open('template.html', mode='r', encoding="utf-8").read())

with codecs.open('www/index.html', mode="w", encoding="utf-8") as fd:
    fd.write(template.render(content=html, date=datetime.date.today(), version=__version__))
