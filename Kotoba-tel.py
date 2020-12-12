import re


num_of_player = 0
num_of_odai = 0
destroyed_card = []
moji = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','へ','ホ','マ','ミ','ム',
        'メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン','ー','濁点','半濁点',
        '小文字','確定','列確定','行確定']


class Card:
    def __init__(self, i):
        self.id = i
        self.moji = moji[i]
        self.cardtype = cardtype_check(i)  # 文字札か特殊札かを記録
        # 確定タイプを記録
        self.fix = False # 文字確定
        self.column_fix = False # 行確定
        self.row_fix = False # 列確定

    # カードが文字札か特殊札かを記録
    def cardtype_check(i):
        if i < 47:
            return 'moji'
        elif i >= 47:
            return 'tokushu'

    # 確定タイプを記録
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
        self.odai = [] # プレイヤーのお題を記録
        self.word_field = [] # 自分が場に出している文字札
        self.tokushu_card = [] # 手札に持っている特殊札
        self.amari_card = [] # 手札に持っている文字札
        self.clear = False # 自分のパートナーのお題を当てられたかどうかを記録

    # お題の言葉を入力
    # 一度お題を自分のところに記録してから，あとで1人分ずつずらしていく？
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

    # 自分のカードを入れ替える

    # 指定したプレイヤーと文字札を交換する

    # カードを破棄する

    # 特殊札をパートナーに渡す

    # 特殊札をパートナーからもらう

    # パートナーのお題を当てる

# プレイヤーの人数を決める
def input_num_of_player():
    while True:
        num_of_player = input('プレイする人数を入力してください >> ')
        if num_of_player.isdigit():
            return num_of_player
        print('数字のみで入力してください')

# お題の文字数を決める
def input_num_of_odai():
    while True:
        num_of_odai = input('お題の文字数を入力してください >> ')
        if num_of_odai.isdigit():
            return num_of_odai
        print('数字のみで入力してください')


# プレイヤーの名前を入力
def input_name():
    while True:
        print('カタカナで8文字以内で入力してください')
        name = input('お名前を入力してください >> ')
        if len(word) <= 8:
            if re.search(r'[ァ-ー]', name):
                return name


# プレイヤーのインスタンスを作成
def make_players():
    players = []
    for i in range(num_of_player):
        players.append(Player(i, input_name()))
    return players


# 山札をシャッフル

# カードを配る

# ドローする
def draw(player_id):



def clear_check():
