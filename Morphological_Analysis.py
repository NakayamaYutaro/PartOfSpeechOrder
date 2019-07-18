#-*- coding: utf-8 -*イ-
import sys
import codecs
import MeCab
from WriteToTxt import write_to_txt 

class mecab_analysis:
    def __init__(self,self.num,f):
        #変数の初期化
        self.l = 0;self.m = 0;self.k = 0;self.cnt = 0;self.flag=0;
        #ファイルの行数をカウントする
        row_num = len(open(f).readlines())
        #曖昧文の品詞順サンプル    
        self.base = ["名詞","動詞","名詞","名詞","助詞","名詞","動詞","名詞","名詞","動詞"]
        #曖昧性判断材料の配列の準備       
        self.order = ["動詞","形容詞","形容動詞","名詞","副詞","連体詞","接続詞","感動詞","助動詞","助詞"]
        #品詞を登録する配列2x10を準備
        self.ar = [[0 for i in range(self.num)] for j in range(2)]
        for i in range(len(self.ar[0])): 
          self.ar[0][i] = i
      
    def mecab_sub(self,read_file):
        line_cnt = 0
        #テキストファイル出力のインスタンスを生成
        t = write_to_txt() 
        #.が出現したら。配列ar[1][all:]=0にして,再度曖昧渡判定をする
        f = open(read_file,'r')
        m = MeCab.Tagger("-Owakati")
        line = f.readline()
        
        while line:
            line_cnt = line_cnt + 1
            #行単位でMecab解析
            res = m.parseToNode(line)
            wakati = m.parse(line)
            print wakati 
            while res:
              #品詞数の設定(文章中の品詞の長さ)
              if(self.k>9):
                self.k = 0
              #リストに変換する
              list_o = res.feature.split(' ')
              #文字化けの回避のためのデコード
              sre = str(list_o).decode('string-escape')
              print sre
              if(sre.count(self.base[self.k])):
                #配列に値を入れる
                self.ar[1][self.k] = 1
                #リストの要素の繰り上げ 
                self.k = self.k + 1;
              else:
                self.k = 0
                for self.l in range(len(self.ar[0])):
                    self.ar[1][self.l] = 0   
              #品詞の一致結果配列を随時表示
              print self.ar
              #配列の要素を足し合わせた結果がself.numならば曖昧性検出
              for g in range(len(self.ar[0])):
                if(self.ar[1][g] == 1):  
                    self.cnt = self.cnt + 1
                    if(self.cnt == self.num): 
                      with open('result_mecab.txt','a') as f:
                        f.write(sre+'\n'+self.ar+'\n')   
                      print """-------------------------------------"""
                      print """!!テキストから曖昧性を検出しました!!"""  
                      print """-------------------------------------"""
                      yield line_cnt
              #cntを0にしないとだめである
              self.cnt = 0
              #文字列をまとめる
              result = str(sre) + str(self.ar) + "\n"
              t.insert_text('se',result) 
              res = res.next 
            line = f.readline()
            print("\n")


    def wakati(self,read_file):
        f = open(read_file,'r')      
        m = MeCab.Tagger("-Owakati")     
        line = f.readline()
        while line:                      
            res = m.parse(line) 
            list_o = res.split(' ') 
            line = f.readline()   
            print(res)
