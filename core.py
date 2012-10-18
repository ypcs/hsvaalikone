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
	def __init__(self):
		pass

class Municipality(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "%s" % self.name

class Party(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "%s" % self.

class Candidate(object):
	def __init__(self, lastname, firstname, party, municipality):
		self.lastname = lastname
		self.firstname = firstname
		self.party = party # TODO: ref Party
		self.municipality = municipality # TODO: ref Municipality

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

def parse_row(d):
	raise NotImplementedError

def main(args):
	# Read full CSV to list
	everything = read_data(args.infile)

	print everything[0:5]

	# TODO: My answers = abcdefg, compare to data, calculate best party match

	return 0

def run():
	parser = argparse.ArgumentParser()

	parser.add_argument('--infile', dest='infile', help="Input filename (HS data as CSV)")

	args = parser.parse_args()
	sys.exit(main(args) or 0)

if __name__ == "__main__":
	run()