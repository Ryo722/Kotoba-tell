import re


num_of_player = 0
num_of_char = 0
deck = 120
destroyed_card = []
moji = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','へ','ホ','マ','ミ','ム',
        'メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン','ー','濁点','半濁点',
        '小文字','確定','列確定','行確定']


class Card:
    def __init__(self, i):
        self.id = i
        self.moji = moji[i]
        self.cardtype = cardtype_check(i)
        self.fix = False
        self.column_fix = False
        self.row_fix = False

    def cardtype_check(i):
        if i < 47:
            return 'moji'
        elif i >= 47:
            return 'tokushu'

    def setting_fix(id):
        if id == 50:
            self.fix = True
        elif id == 51:
            self.column_fix = True
        else:
            self.row_fix = True

    def get_id():
        return self.id

    def get_moji():
        return self.moji
    
    def get_cardtype():
        return self.cardtype

    def get_fixtype():
        return self.fix, self.column_fix, self.row_fix
    


class Player:
    def __init__(self, i, name):
        self.player_id = i
        self.player_name = name
        self.word_field = []
        self.tokushu_card = []
        self.amari_card = []
        self.clear = False
    
    def define_word(num_of_char):
        while len(word_field == 0):
            print('カタカナと伸ばし棒のみで', num_of_char, '文字で入力してください')
            word = input('右隣の人のお題 >> ')
            if len(word) == num_of_char:
                if re.search(r'[ァ-ー]', word):
                    self.word_field.append()
                else:
                    print("カタカナと伸ばし棒のみで入力してください")
            else:
                print(num_of_char, "文字で入力してください")


def input_name():
    while True:
        print('カタカナで8文字以内で入力してください')
        name = input('お名前を入力してください >> ')
        if len(word) <= 8:
            if re.search(r'[ァ-ー]', name):
                return name

def make_players():
    players = []
    for i in range(num_of_player):
        players.append(Player(i, input_name()))
    return players

    
def clear_check():
