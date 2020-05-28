import warnings
warnings.filterwarnings('ignore')

#-*- coding:utf-8 _*-

import codecs
from dataset import dataset
from model import HMM

if __name__ == "__main__":
    dataset = dataset()
    dataset.remove_space('test_cws1.txt','row_cws.txt')
    fin = codecs.open('row_cws.txt','r','utf-8')
    fout = codecs.open('test_cws2.txt','w','utf-8')
    train_data =  open('train_cws.txt','r', encoding='utf-8')
    model_file = 'hmm.pkl'
    hmm = HMM()

    # 分词
    hmm.train(train_data,model_file)
    hmm.load_model(model_file)
    for line in fin.readlines():
        print(line)

        hmm.cut(line.strip(),outfile=fout)
        print('-'*30)
    fin.close()
    fout.close()










