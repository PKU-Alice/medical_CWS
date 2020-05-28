#-*-coding:utf-8 -*-

class HMM(object):

    def __init__(self):
        self.state_list = ['B','M','E','S']
        self.start_p = {}
        self.trans_p = {}
        self.emit_p = {}

        self.model_file = 'hmm_model.pkl'
        self.trained = False

    def train(self,datas,model_path=None):
        if model_path == None:
            model_path = self.model_file
        #统计状态频数
        state_dict = {}

        def init_parameters():
            for state in self.state_list:
                self.start_p[state] = 0.0
                self.trans_p[state] = {s:0.0 for s in self.state_list}
                self.emit_p[state] = {}
                state_dict[state] = 0

        init_parameters()

        def make_label(text):
            out_text = []
            if len(text) == 1:
                out_text = ['S']
            else :
                out_text += ['B']+['M']*(len(text)-2)+['E']
            return out_text


        line_nb = 0

        #监督学习方法求解参数，详情见统计学习方法10.3.1节
        for line in datas:
            line = line.strip()
            if not line:
                print(line)
            line_nb += 1

            word_list = [w for w in line if w != ' ']
            line_list = line.split()
            line_state = []
            for w in line_list:
                line_state.extend(make_label(w))

            assert len(line_state) == len(word_list)

            for i,v in enumerate(line_state):
                state_dict[v] += 1

                if i == 0:
                    self.start_p[v] += 1
                else :
                    self.trans_p[line_state[i-1]][v] += 1
                    self.emit_p[line_state[i]][word_list[i]] = self.emit_p[line_state[i]].get(word_list[i],0)+1.0

        self.start_p = {k: v*1.0/line_nb for k,v in self.start_p.items()}
        self.trans_p = {k:{k1: v1/state_dict[k1] for k1,v1 in v0.items()} for k,v0 in self.trans_p.items()}
        self.emit_p = {k:{k1: (v1+1)/state_dict.get(k1,1.0) for k1,v1 in v0.items()} for k,v0 in self.emit_p.items()}

        with open(model_path,'wb') as f:
            import pickle
            pickle.dump(self.start_p,f)
            pickle.dump(self.trans_p,f)
            pickle.dump(self.emit_p,f)
        self.trained = True

        print('model train done,parameters save to ',model_path)

    #读取参数模型
    def load_model(self,path):
        import pickle
        with open(path,'rb') as f:
            self.start_p = pickle.load(f)
            self.trans_p = pickle.load(f)
            self.emit_p = pickle.load(f)
        self.trained = True
        print('model parameters load done!')

    #维特比算法求解最优路径 ，详情见统计学方法10.4.2节
    def __viterbi(self,text,states,start_p,trans_p,emit_p):
        V = [{}]
        path = {}

        for y in states:
            V[0][y] = start_p[y]*emit_p[y].get(text[0],1.0)
            path[y] = [y]

        #print('初始的path是：',path)


        for t in range(1,len(text)):
            V.append({})
            new_path = {}
            #print('第',t,'个V是：',V)


            for j in states:
                emitp = emit_p[j].get(text[t],1.0)
                # print(emitp)

                (prob , state) = max([(V[t - 1][i] * trans_p[i].get(j, 0) * emitp, i)
                                      for i in states if V[t - 1][i] > 0])


                V[t][j] = prob

                new_path[j] = path[state]+[j]
                #print(new_path)

            path = new_path

        # 最后一步
        (prob,state) = max([(V[len(text)-1][y],y) for y in states])

        return (prob,path[state])

    def cut(self,text,outfile):
        prob,pos_list = self.__viterbi(text,self.state_list,self.start_p,self.trans_p,self.emit_p)
        print(pos_list)

        for i, char in enumerate(text):
            pos = pos_list[i]
            if pos == 'E' or pos=='S':
                outfile.write(char+' ')
            else:
                outfile.write(char)



















































