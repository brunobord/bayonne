#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs

import markdown
from jinja2 import Template

text = codecs.open("index.md", mode="r", encoding="utf-8").read()
html = markdown.markdown(text, extensions=['headerid'])

template = Template(codecs.open('template.html', mode='r', encoding="utf-8").read())

with codecs.open('www/index.html', mode="w", encoding="utf-8") as fd:
    fd.write(template.render(content=html))
