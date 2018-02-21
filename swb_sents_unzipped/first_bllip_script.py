#!/usr/bin/env python

"""Author: Roman Ziserman"""

"""This script iterates over all the files in a directory containing siwtchboad data files (text).
It parses each individual sentence in every file and produces an output text file containing an nbest list of
20 parses. The text files are named using the convention 'fileid.sentid.txt'"""
import os
import time

from bllipparser import RerankingParser
rrp = RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

#Time the execution of this script
t0 = time.time()

#For readability
parsed_dir = os.getcwd() + '/parsed/' #parsed sentences will be stored here
sents_dir = os.getcwd() + '/swb_sents/' #directory where sentences are stored

#list to hold the sentences from the txt file. This list will be processed by the parser.
sentences = []

#list to hold sentence ids
sent_id_list = []

"""keep track of the current file being processed; used to create output file name. Will concatenate with
the sentence IDs"""
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
					sent_id_list.append(curr_line.strip('\n').strip('\r'))
					continue
				sentences.append(curr_line.strip('\n').strip('\r'))
	
		#Remove all the empty strings (in python3, wrap filter() in list()
		sentences = filter(None, sentences)

		"""This loop will parse each sentence in the sentences list and store them in a text file.
		It will stored in the parsed folder"""
		for curr_sent in range(len(sentences)):
			nbest_list = rrp.parse(sentences[curr_sent])
			#create a file name for the current sentence
			out_file_name = curr_file[:-9] + "." + sent_id_list[curr_sent]  + '.txt'
			
			#dump the file into the parsed directory
			with open(parsed_dir + out_file_name, 'w') as output:
				print>>output, nbest_list

		#reset both sentence and sentenceID lists for next iteration
		sentences = [] 
		sent_id_list = []
		
		t1= time.time()
		elapsed = t1-t0

		with open(parsed_dir + 'TOTAL_RUN_TIME.txt', 'w') as tot_time:
			print>>tot_time, "Total runtime: " + str(elapsed) 
except IOError as err:
	print('File error:' + str(err))
