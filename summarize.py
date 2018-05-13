#R为句子集，S为句子，w(S)为句子的权重，也就是每个单词权重的求和。Cn为第n个句子的代价，也就是第n个句子的长度（单词量）
#每个单词的权重w=tf*idf，tf为单词在本篇文章中的词频，idf为单词出现过的文章占总文章的比重的倒数再求对数（以十为底）
#停用词来源：https://blog.csdn.net/shijiebei2009/article/details/39696523
import re

class Summarize:
    stopword = []
    input_path = r''
    input_text = ''


    def __init__(self, path):
        self.input_path = path
        stopword_path = r'C:\Code\Python\summarization\summary\stopword.txt'
        with open(stopword_path, 'r') as stopword_file:
            self.stopword = stopword_file.readlines()
            #去除换行符
            for i in range(0, len(self.stopword)):
                self.stopword[i] = self.stopword[i].strip()
                self.stopword[i] = self.stopword[i].strip('\n')
        print(self.stopword)
        with open(self.input_path, 'r') as input_file:
            self.input_text = input_file.read()


    #去除停用词，不可去除标点符号，因为需要作为句子的分界
    def clear(self):
        print(self.input_text)
        for word in self.stopword:
            self.input_text = self.input_text.replace(' ' + word + ' ', ' ')
            if self.input_text.endswith(word, 0, len(word)):
                self.input_text = self.input_text[len(word):]
                self.input_text = self.input_text.strip()
            if self.input_text.endswith(word):
                self.input_text = self.input_text[:-len(word)]
                self.input_text = self.input_text.strip()
        print(self.input_text)
        self.split_sentence(self.input_text)

    def split_sentence(self, text):
        sentences = re.split(r'\.\s|,\s|:\s|\?\s', text)
        print(sentences)




if __name__ == '__main__':
    summarize = Summarize(r"C:\Code\Python\summarization\output\600340\758228292_业绩靓丽，成长延续_2018-05-02.txt")
    summarize.clear()

