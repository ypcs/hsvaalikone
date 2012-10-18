#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>
# Code is licensed under GPLv3, for source data see README.md

import os
import sys
import argparse
import csv

CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'

class Question(object):
	def __init__(self, question, answer, weight, comment):
		self.question = question
		self.answer = answer
		self.weight = weight
		self.comment = comment
	
	def __str__(self):
		return "Question: %s\nAnswer: %s\nWeight: %s\nComment: %s" % (self.question, self.answer, self.weight, self.comment)

class Municipality(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "%s" % self.name

class Party(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "%s" % self.name

class Candidate(object):
	def __init__(self, lastname, firstname, party, municipality, age, www, facebook, twitter):
		self.lastname = lastname
		self.firstname = firstname
		self.party = party # TODO: ref Party
		self.municipality = municipality # TODO: ref Municipality
		self.age = age
		self.www = www
		self.twitter = twitter
		self.facebook = facebook

	def __str__(self):
		return "%s, %s (%s) / %s" % (self.lastname, self.firstname, self.party, self.municipality)

def read_data(filename, quotechar=CSV_QUOTECHAR, delimiter=CSV_DELIMITER):
	if not os.path.exists(filename):
		raise IOError, 'File not found: %s' % filename
	reader = csv.reader(open(filename, 'r'), quotechar=quotechar, delimiter=delimiter)

	data = []

	for row in reader:
		data.append(row)
	return data

def parse_row(row):
	candidate = Candidate(row.pop(0), row.pop(0), row.pop(0), row.pop(0), row.pop(0), row.pop(0), row.pop(0), row.pop(0));
	questions = []
	
	for i in range(0, len(row)-3, 4):
		question = Question(row[i+0], row[i+1], row[i+2], row[i+3])
		questions.append(question)
		
	return candidate, questions

def main(args):
	# Read full CSV to list
	everything = read_data(args.infile)

	# Pick the second candidate in the list and print her information:
	parsed_row = parse_row(everything[2]);
	candidate = parsed_row[0]
	questions = parsed_row[1]
	print candidate
	for	question in questions:
		print question, "\n"

	# TODO: My answers = abcdefg, compare to data, calculate best party match

	return 0

def run():
	parser = argparse.ArgumentParser()

	parser.add_argument('--infile', dest='infile', help="Input filename (HS data as CSV)")

	args = parser.parse_args()
	sys.exit(main(args) or 0)

if __name__ == "__main__":
	run()