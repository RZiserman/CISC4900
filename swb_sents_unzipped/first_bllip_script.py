#!/usr/bin/env python

"""Author: Roman Ziserman"""

import os

from bllipparser import RerankingParser
rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

parsed_dir = os.getcwd() + '/parsed/' #parsed sentences will be stored here
sents_dir = os.getcwd() + '/swb_sents/' #directory where sentences are stored

#list  hold the sentences from the txt file. This list will be processed by the parser.
sentences = []

#counter to keep track of the current sentence for parsed files
curr_sent_num = 1

"""keep track of the current file being processed; used to create output file name.Will concatenate with
current_Sent_num"""
out_file_name= None 

"""list of files in swb_Sents directory. Will be used to  process all the files in the following loop."""
sent_dir_files = os.listdir(os.getcwd() + '/swb_sents') 

try:
	#The following for loop builds a list of sentences from the text file being processed
	for curr_file in sent_dir_files:
		with open(sents_dir + curr_file) as data:
			for curr_line in data:
				#skip all the #sentN stuff
				if '#' in curr_line: 
					continue
				sentences.append(curr_line.strip('\n').strip('\r'))
	
		#Remove all the empty strings (in python3, wrap filter() in list()
		sentences = filter(None, sentences)

		"""This loop will parse each sentence in the sentences list and build a pickle file.
		It will stored in the parsed folder"""
		for curr_sent in sentences:
			nbest_list = rrp.parse(curr_sent)
			#create a file name for the current sentence
			out_file_name = curr_file[:-9] + ".Sentence#" + str(curr_sent_num) + '.txt'
			curr_sent_num = curr_sent_num + 1
			
			#dump the file into the parsed directory
			with open(parsed_dir + out_file_name, 'w') as output:
				print>>output, nbest_list

		#reset sentence list for next iteration
		curr_sent_num = 1 
		#reset sentence list for next iteration
		sentences = [] 
		
except IOError as err:
	print('File error:' + str(err))
