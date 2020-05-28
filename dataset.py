import codecs
import re

class dataset(object):

    def remove_space(self,fin1,fout1):
        fin = codecs.open(fin1,'r','utf-8')
        fout = codecs.open(fout1,'w','utf-8')
        for s in fin.readlines():
            fout.writelines(s.replace(' ',''))
        fin.close()
        fout.close()
        return

    def character_tagging(self,input_file,output_file):
        input_data = codecs.open(input_file,'r','utf-8')
        output_data = codecs.open(output_file,'w','utf-8')

        for line in input_data.readlines():
            word_list = line.strip().split()
            for word in word_list:
                if len(word) == 1:
                    output_data.write(word + '\tS\n')
                else:
                    output_data.write(word[0] + '\tB\n')
                    for w in word[1:len(word)-1]:
                        output_data.write(w + '\tM\n')
                    output_data.write(word[len(word)-1] + '\tE\n')
            # output_data.write('\n')

        input_data.close()
        output_data.close()

    def ner_dataset(self,input_file,output_file):
        input_data = codecs.open(input_file,'r','utf-8')
        output_data = codecs.open(output_file,'w','utf-8')
        for line in input_data.readlines():
            simple = re.compile('[[](.*?)[]]bod[1]',re.S|re.M).findall(line)
            for word in simple:
                word = word.strip().split()
                if len(word) == 1:
                    output_data.write(word[0].replace('[','') + '\tB-bod\n')
                else:
                    output_data.write(word[-1].replace('[','') + '\tB-bod\n')





