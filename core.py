#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Parsing HS candidate data'''

# (c) 2012 Ville Korhonen <ville@xd.fi>
# Code is licensed under GPLv3, for source data see README.md

import os
import sys
import argparse
import csv

CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'

class Question(object):
    '''Single question'''
    def __init__(self, question, answer, weight, comment):
        self.question = question
        self.answer = answer
        self.weight = weight
        self.comment = comment
    
    def __str__(self):
        return "Question: %s\nAnswer: %s\nWeight: %s\nComment: %s" % (
            self.question,
            self.answer,
            self.weight,
            self.comment)

class Municipality(object):
    '''Municipality'''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s" % self.name

class Party(object):
    '''Political party'''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "%s" % self.name

class Candidate(object):
    '''Election candidate'''
    def __init__(self, lastname, firstname, party, *args, **kwargs):
        self.lastname = lastname
        self.firstname = firstname
        self.party = party # TODO: ref Party

        if 'municipality' in kwargs:
            self.municipality = kwargs['municipality'] # TODO: ref Municipality
        
        if 'age' in kwargs:
            self.age = kwargs['age']
        
        if 'url' in kwargs:
            self.url = kwargs['url']
        
        if 'twitter_url' in kwargs:
            self.twitter_url = kwargs['twitter_url']
        
        if 'facebook_url' in kwargs:
            self.facebook_url = kwargs['facebook_url']

    def __str__(self):
        return "%s, %s (%s) / %s" % (self.lastname,
            self.firstname,
            self.party,
            self.municipality)

def read_data(filename, quotechar=CSV_QUOTECHAR, delimiter=CSV_DELIMITER):
    if not os.path.exists(filename):
        raise IOError, 'File not found: %s' % filename
    reader = csv.reader(open(filename, 'r'),
        quotechar=quotechar,
        delimiter=delimiter)

    data = []

    for row in reader:
        data.append(row)
    return data

def parse_row(row):
    candidate = Candidate(municipality=row.pop(0),
        party=row.pop(0),
        lastname=row.pop(0),
        firstname=row.pop(0),
        age=row.pop(0),
        url=row.pop(0),
        facebook_url=row.pop(0),
        twitter_url=row.pop(0))
    questions = []
    
    for i in range(0, len(row)-3, 4):
        question = Question(question=row[i+0],
            answer=row[i+1],
            weight=row[i+2],
            comment=row[i+3])
        questions.append(question)
        
    return candidate, questions

def main(args):
    # Read full CSV to list
    everything = read_data(args.infile)

    # Pick the second candidate in the list and print her information:
    candidate, questions = parse_row(everything[2])
    
    print candidate
    for question in questions:
        print question, "\n"

    # TODO: My answers = abcdefg, compare to data, calculate best party match

    return 0

def run():
    '''Initialize ArgumentParser & execute main'''
    parser = argparse.ArgumentParser()

    parser.add_argument('--infile',
        dest='infile',
        help="Input filename (HS data as CSV)")
    parser.add_argument('--municipality',
        dest='use_municipality',
        help="Restrict answers to single municipality",
        default=None,
        metavar='MUNICIPALITY')

    args = parser.parse_args()
    sys.exit(main(args) or 0)

if __name__ == "__main__":
    run()