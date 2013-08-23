#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs
import json

import requests
from fabric.api import local, task, run, cd


@task
def build():
    "Build the website"
    local('python build.py')


@task
def download():
    "Download the GeoJSON map"
    req = requests.get('https://gist.github.com/brunobord/6206708/raw/map.geojson')
    data = json.loads(req.text)
    with codecs.open('map.geojson', mode="w", encoding="utf-8") as geojson:
        geojson.write(json.dumps(data, indent=3))


@task
def update():
    "Update the website"
    with cd('vhosts/jehaisleprintemps/bayonne/'):
        run('git pull')


@task
def all():
    "Do the whole shebang"
    build()
    download()
    update()
