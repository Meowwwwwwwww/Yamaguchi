import random
import numpy as np

Gua_name = [
    ['第2卦:坤','第23卦: 剥','第8卦:比','第20卦: 观','第16卦: 豫','第35卦: 晋','第45卦: 萃','第12卦: 否'],
    ['第15卦: 谦','第52卦: 艮','第39卦: 蹇','第53卦: 渐','第62卦: 小过','第56卦: 旅','第31卦: 咸','第33卦: 遁'],
    ['第7卦: 师','第4卦:蒙','第29卦: 坎','第59卦: 涣','第40卦: 解','第64卦: 未济','第47卦: 困','第6卦:讼'],
    ['第46卦: 升','第18卦: 蛊','第48卦: 井','第57卦: 巽','第32卦: 恒','第50卦: 鼎','第28卦: 大过','第44卦: 姤'],
    ['第24卦: 复','第27卦: 颐','第3卦:屯','第42卦: 益','第51卦: 震','第21卦: 噬嗑','第17卦: 随','第25卦: 无妄'],
    ['第36卦: 明夷','第22卦: 贲','第63卦: 既济','第37卦: 家人','第55卦: 丰','第30卦: 离','第49: 革','第13卦: 同人'],
    ['第19卦: 临','第41卦: 损','第60卦: 节','第61卦: 中孚','第54卦: 归妹','第38卦: 睽','第58卦: 兑','第10卦: 履'],
    ['第11卦: 泰','第26卦: 大畜','第5卦:需','第9卦:小畜','第34卦: 大壮','第14卦: 大有','第43卦: 夬','第1卦:乾']
            ]

Gua_explain =[
    ['http://baike.fututa.com/a5739/', 'http://baike.fututa.com/a5760/', 'http://baike.fututa.com/a5745/',
     'http://baike.fututa.com/a5757/', 'http://baike.fututa.com/a5753/', 'http://baike.fututa.com/a5772/',
     'http://baike.fututa.com/a5782/', 'http://baike.fututa.com/a5749/'],
    ['http://baike.fututa.com/a5752/', 'http://baike.fututa.com/a5789/', 'http://baike.fututa.com/a5776/',
     'http://baike.fututa.com/a5790/', 'http://baike.fututa.com/a5799/', 'http://baike.fututa.com/a5799/',
     'http://baike.fututa.com/a5768/', 'http://baike.fututa.com/a5770/'],
    ['http://baike.fututa.com/a5744/', 'http://baike.fututa.com/a5741/', 'http://baike.fututa.com/a5766/',
     'http://baike.fututa.com/a5796/', 'http://baike.fututa.com/a5777/', 'http://baike.fututa.com/a5801/',
     'http://baike.fututa.com/a5784/', 'http://baike.fututa.com/a5743/'],
    ['http://baike.fututa.com/a5761/', 'http://baike.fututa.com/a5755/', 'http://baike.fututa.com/a5785/',
     'http://baike.fututa.com/a5794/', 'http://baike.fututa.com/a5769/', 'http://baike.fututa.com/a5787/',
     'http://baike.fututa.com/a5765/', 'http://baike.fututa.com/a5781/'],
    ['http://baike.fututa.com/a5761/', 'http://baike.fututa.com/a5764/', 'http://baike.fututa.com/a5740/',
     'http://baike.fututa.com/a5779/', 'http://baike.fututa.com/a5788/', 'http://baike.fututa.com/a5758/',
     'http://baike.fututa.com/a5754/', 'http://baike.fututa.com/a5762/'],
    ['http://baike.fututa.com/a5773/', 'http://baike.fututa.com/a5759/', 'http://baike.fututa.com/a5800/',
     'http://baike.fututa.com/a5774/', 'http://baike.fututa.com/a5792/', 'http://baike.fututa.com/a5767/',
     'http://baike.fututa.com/a5786/', 'http://baike.fututa.com/a5750/'],
    ['http://baike.fututa.com/a5756/', 'http://baike.fututa.com/a5778/', 'http://baike.fututa.com/a5797/',
     'http://baike.fututa.com/a5798/', 'http://baike.fututa.com/a5791/', 'http://baike.fututa.com/a5775/',
     'http://baike.fututa.com/a5795/', 'http://baike.fututa.com/a5747/'],
    ['http://baike.fututa.com/a5748/', 'http://baike.fututa.com/a5763/', 'http://baike.fututa.com/a5742/',
     'http://baike.fututa.com/a5746/', 'http://baike.fututa.com/a5771/', 'http://baike.fututa.com/a5751/',
     'http://baike.fututa.com/a5780/', 'http://baike.fututa.com/a5738/']
]

def guidance(change):
    if change == 0:
        return ('朱熹曰:六爻皆不变者，占本卦卦辞.')
    elif change == 1:
        return('朱熹曰:一爻变者，以本卦变爻之辞占.')
    elif change == 2:
        return ('朱熹曰:二爻变者，以本卦二变爻之辞占，而以上爻之辞为主')
    elif change == 3:
        return ('朱熹曰:三爻变者，占本卦及之卦的卦辞，而以本卦为主')
    elif change == 4:
        return ('朱熹曰:四爻变者，以之卦中二不变之爻辞占')
    elif change == 5:
        return ('朱熹曰:五爻变者，以之卦中不变爻的爻辞占')
    elif change == 6:
        return ('朱熹曰:六爻皆变者，以乾坤二用之辞占，并参考其之卦卦辞')

def Getguaxiang():
    text = []
    guaxiang = []
    i = 0
    m = 0
    while i < 6:
        number = 49
        j = 0
        while j < 3:
            k = random.randint(2, number)
            l = number - k
            number = number - 1
            k1 = (k - 1) % 4
            l1 = l % 4
            if k1 == 0:
                number = number - 4
            else:
                number = number - k1
            if l1 == 0:
                number = number - 4
            else:
                number = number - l1
            m = m + 1
            j = j + 1
        if number == 24:
            guaxiang.insert(0, 6)
        elif number == 28:
            guaxiang.insert(0, 7)
        elif number == 32:
            guaxiang.insert(0, 8)
        elif number == 36:
            guaxiang.insert(0, 9)
        i = i + 1

    p = 0
    bengua = []
    while p < 6:
        if (guaxiang[p] == 7 or guaxiang[p] == 9):
            bengua.append(1)
            text.append('------------------------')
        elif (guaxiang[p] == 6 or guaxiang[p] == 8):
            bengua.append(0)
            text.append('--------          --------')
        p = p + 1
    q = 0
    zhigua = []
    biangua = []
    change = 0
    while q < 6:
        if (guaxiang[q] == 6 or guaxiang[q] == 9):
            biangua.append(q+1)
            var = 1 - bengua[q]
            change = change + 1
            zhigua.append(var)
            if var == 1:
                text.append('------------------------')
            else:
                text.append('--------          --------')
        if (guaxiang[q] == 7 or guaxiang[q] == 8):
            zhigua.append(bengua[q])
            if bengua[q] == 1:
                text.append('------------------------')
            else:
                text.append('--------          --------')
        q = q + 1
    z = 0
    guide = guidance(change)
    text.append(guide)
    return text

def numberize(text):
    if(text == '000'):
        return 0
    elif (text == '001'):
        return 1
    elif (text == '010'):
        return 2
    elif (text == '011'):
        return 3
    elif (text == '100'):
        return 4
    elif (text == '101'):
        return 5
    elif (text == '110'):
        return 6
    elif (text == '111'):
        return 7



def decoding(text):
    text_word = []
    i = 0
    while i < 12:
        if text[i] == '--------          --------':
            text_word.append('0')
        if text[i] == '------------------------':
            text_word.append('1')
        i = i + 1
    ben_high = ''
    ben_low = ''
    zhi_high = ''
    zhi_low = ''
    j = 5
    while j > 2:
        ben_high = ben_high + text_word[j]
        j = j - 1
    k = 2
    while k >= 0:
        ben_low = ben_low + text_word[k]
        k = k - 1
    l = 11
    while l > 8:
        zhi_high = zhi_high + text_word[l]
        l = l - 1
    m = 8
    while m >= 6:
        zhi_low = zhi_low + text_word[m]
        m = m - 1
    ben_high_num = numberize(ben_high)
    ben_low_num = numberize(ben_low)
    zhi_high_num = numberize(zhi_high)
    zhi_low_num = numberize(zhi_low)
    bengua_real = Gua_name[ben_high_num][ben_low_num]
    zhigua_real = Gua_name[zhi_high_num][zhi_low_num]
    bengua_exp = Gua_explain[ben_high_num][ben_low_num]
    zhigua_exp = Gua_explain[zhi_high_num][zhi_low_num]
    return [bengua_real, zhigua_real, bengua_exp, zhigua_exp]


