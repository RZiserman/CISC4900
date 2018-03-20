import os
from sys import argv


if __name__=="__main__":
	incorrect_root_count=0
	num_trees_total=0
	discard_if_root_count_not_1=True
	if len(argv)<3:
		print("please input the path to the file that needs to be cleaned and output file path")
		print("Example: %s train.conll train-cleaned.conll"%argv[0])
	else:
		#input_fpath="train.conll"
		#output_fpath="train-cleaned.conll"
		input_fpath=argv[1]
		output_fpath=argv[2] 
		
		fopen=open(input_fpath)		
		out_fopen=open(output_fpath,"w")

		cur_set=[]
		for fi, f in enumerate(fopen):		
			line_strip=f.strip("\n\r\t ")
			split=line_strip.split("\t")
			if line_strip!="": cur_set.append(split)
			else: 
				if cur_set !=[]:
					num_trees_total+=1
					labels_as_as=[v[7] for v in cur_set]
					#if "ROOT" in labels_as_as:
					#	print labels_as_as
					labels=[v[7].lower() for v in cur_set]
					#print labels
					if labels.count("root")!=1 or not discard_if_root_count_not_1:
						#print ">>>>", labels
						incorrect_root_count+=1
						for cs in cur_set:
							print cs
							
						print '----'
					else:
						for cs in cur_set:
							line="\t".join(cs)+"\n"
							out_fopen.write(line)
						out_fopen.write("\n")
					
					cur_set=[]

		fopen.close()

		out_fopen.close()
		print "total number of trees processed", num_trees_total
		print "number of discarded trees", incorrect_root_count