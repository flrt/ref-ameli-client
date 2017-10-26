#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Client de consultation des flux ATOM du référentiel AMELI

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import datetime
import io

import lxml.etree
import requests


def infos_entries(entry):
    """Affiche les informations sur les données à télécharger pour 1 entrée = 1 version"""
    ae = AtomEntry(entry)

    version_txt = "Version : {} du {}".format(ae.version(),
                                              ae.updated().strftime("%d/%m/%Y"))
    print("  {}".format(version_txt))
    print("  {}".format(len(version_txt) * "="))

    print("  Liens à télécharger")
    for link in ae.links():
        print("    {}".format(link))
    print()


class Checker:
    def __init__(self, url):
        self.url = url
        self.feeddata = None

    def load_feed(self):
        """Lecture du flux ATOM et parsing XML"""
        data = requests.get(self.url)
        if data.status_code == 200:
            self.feeddata = lxml.etree.parse(io.StringIO(data.text))

    def get_updated_feed(self):
        """Recupere la date de dernière mise à jour du flux ATOM"""
        if not self.feeddata:
            self.load_feed()
        NS = {'a': 'http://www.w3.org/2005/Atom'}
        strdate = self.feeddata.xpath('/a:feed/a:updated/text()', namespaces=NS)[0]

        feed_last_updated = datetime.datetime.strptime(strdate[:19], "%Y-%m-%dT%H:%M:%S")
        return feed_last_updated

    def entries_post_version(self, version):
        """
        Selectionne les entrées dont le numéro de version est postérieur à celui passé en paramètre
        Les entrées ATOM ont 1 id contenant la version
        ex : urn:ameli:lpp:v467
             urn:ameli:ccam:v49

        :param version: numero de version, ex: 40
        :return: liste des entrées ATOM type: List
        """
        if not self.feeddata:
            self.load_feed()

        result = []

        for entry in self.feeddata.xpath('//a:entry', namespaces={'a': 'http://www.w3.org/2005/Atom'}):
            ae = AtomEntry(entry)
            if float(ae.version()) > float(version):
                result.append(entry)

        return result

    def entries_post_date(self, stringdate):
        """
        Sélectionne les entrées dont la date est postérieure à celui passée en paramètre

        :param stringdate: date de la version au format YYYY-MM-dd
        :return: liste des entrées ATOM type: List
        """
        if not self.feeddata:
            self.load_feed()

        result = []
        basedate = datetime.datetime.strptime(stringdate, "%Y-%m-%d")

        for entry in self.feeddata.xpath('//a:entry', namespaces={'a': 'http://www.w3.org/2005/Atom'}):
            ae = AtomEntry(entry)
            if ae.updated() > basedate:
                result.append(entry)

        return result

    def infos_entries_post_version(self, version):
        """Affiche les informations sur les entrées postérieure à la version demandée"""
        print()
        entries = self.entries_post_version(version)
        print("Nombre d'entrées avec une version supérieure à {} : {}".format(version, len(entries)))
        [infos_entries(entry) for entry in entries]

    def infos_entries_post_date(self, date):
        """Affiche les informations sur les entrées postérieure à la date demandée"""
        print()
        entries = self.entries_post_date(date)
        print("Nombre d'entrées avec une date supérieure à {} : {}".format(date, len(entries)))
        [infos_entries(entry) for entry in entries]


class AtomEntry:
    """
    Classe utilitaire pour accéder aux données d'une Entry Atom
    """

    def __init__(self, entry):
        self.entry = entry
        self.NS = {'a': 'http://www.w3.org/2005/Atom'}

    def id(self):
        return self.entry.xpath('./a:id/text()', namespaces=self.NS)[0]

    def version(self):
        current = self.id()
        return current.split(':')[-1][1:]

    def links(self):
        return self.entry.xpath('./a:link/@href', namespaces=self.NS)

    def updated(self):
        fulldate = self.entry.xpath('./a:updated/text()', namespaces=self.NS)[0]
        return datetime.datetime.strptime(fulldate[:19], "%Y-%m-%dT%H:%M:%S")
