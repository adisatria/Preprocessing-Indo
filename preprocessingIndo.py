import re, csv
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory1 = StopWordRemoverFactory()
stopword = factory1.create_stop_word_remover()

factory2 = StemmerFactory()
stemmer = factory2.create_stemmer()

def tokenWordbase(verse):
    return verse.split(' ')


    # punctuation
def punctuation(tokens):
    tokens = re.sub(r'[>)}:{",?+ !.(<;1234567890]','',str(tokens))
    tokens = re.sub('\n','',str(tokens))
    return tokens


def main():
    currentString = []
    panjangTang = []
    with open('data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0] == '' or row[0] == '-':
                continue
            else:
                tokennya = tokenWordbase(row[0])
                panjangTangSementara = []
                for j in range(len(tokennya)):
                    # print(childToken)
                    puntu = punctuation(tokennya[j])
                    stopnya = stopword.remove(puntu)
                    if stopnya == '':
                        continue
                    else:
                        stemmnya = stemmer.stem(stopnya)
                        currentString.append(stemmnya)
                        panjangTangSementara.append(stemmnya)
                panjangTang.append(panjangTangSementara)
    daftarDokumen = Counter(currentString)
    daftarString = []

    for key, val in daftarDokumen.items():  # melompati(loop over) key di kamus
        if key not in daftarString:
            daftarString.append(key)  # append untuk menambah objek word baru kedalam list
    print(daftarString)
main()