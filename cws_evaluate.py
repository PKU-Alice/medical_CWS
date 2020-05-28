from dataset import dataset
import pandas

if __name__ == '__main__':
    dataset = dataset()
    dataset.character_tagging('test_cws1.txt','test_cws.txt')
    dataset.character_tagging('test_cws2.txt','test_cws3.txt')

    line = []
    line2 = []
    file = open('test_cws.txt',encoding='utf-8')
    file2 = open('test_cws3.txt',encoding='utf-8')

    for i in file.readlines():
        i = i[0:-1]
        if len(i)!=0 and len(i)!=1:
            line.append(i.split('\t'))

    df = pandas.DataFrame(line,columns=['character','train'])

    for i in file2.readlines():
        i = i[0:-1]
        if len(i) != 0 and len(i) != 1:
            line2.append(i.split('\t'))

    df2 = pandas.DataFrame(line2,columns=['character','test'])

    correct = df2[df.train == df2.test]


    for i in ('B','M','E','S'):
        R = sum(correct.test == i)/sum(df.train == i)       # 召回率
        P = sum(correct.test == i)/sum(df2.test == i)       # 准确率
        F = R*P*2/(R+P)                                     # F值
        print(i, ':\n', 'R=', R, ' P=', P, ' F=', F)


