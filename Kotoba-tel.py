import re
from random import shuffle


num_of_player = 0
num_of_odai = 0
moji = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'へ', 'ホ', 'マ', 'ミ', 'ム',
        'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ー', '濁点', '半濁点',
        '小文字', '確定', '列確定', '行確定']


class Card:
    def __init__(self, i):
        self.id = i
        self.moji = moji[i]
        self.cardtype = cardtype_check(i)  # 文字札か特殊札かを記録

        # 濁点,半濁点,小文字を記録
        self.dakuten = False
        self.handaku = False
        self.komoji = False

        # 確定タイプを記録
        self.fix = False  # 文字確定
        self.column_fix = False  # 行確定
        self.row_fix = False  # 列確定

    # カードが文字札か特殊札かを記録
    def cardtype_check(i):
        if i < 47:
            return 'moji'
        elif i >= 47:
            return 'tokushu'

    # 特殊札を設定
    def setting_tokusyu(id):
        if id == 47:
            self.dakuten = True
        elif id == 48:
            self.handaku = True
        elif id == 49:
            self.komoji = True
        elif id == 50:
            self.fix = True
        elif id == 51:
            self.column_fix = True
        else:
            self.row_fix = True

'''
    def get_id():
        return self.id

    def get_moji():
        return self.moji

    def get_cardtype():
        return self.cardtype

    def get_fixtype():
        return self.fix, self.column_fix, self.row_fix
'''


class Deck:
    def __init__(self):
        # Deckを作成
        self.cards = []
        for i in range(47):
            self.cards.extend([Card(i), Card(i)])
        self.cards.extend([Card(47), Card(47), Card(47), Card(47), Card(47), Card(47)])
        self.cards.extend([Card(48), Card(48), Card(48)])
        self.cards.extend([Card(49), Card(49), Card(49)])
        self.cards.extend([Card(50), Card(50), Card(50), Card(50), Card(50), Card(50)])
        self.cards.extend([Card(51), Card(51), Card(51), Card(51)])
        self.cards.extend([Card(52), Card(52), Card(52), Card(52)])

        # 最後にシャッフルする
        shuffle(self.cards)

'''
    # Deckの末尾からcard_numの枚数分ドローする
    def get_card(self, card_num=1):
        self.card_list = []

        if len(self.cards) == 0:
            return

        # card_numの枚数だけDeckからカードをpopする
        for index in range(card_num):
            self.card_list.append(self.cards.pop())
        return self.card_list
'''


class Player:
    def __init__(self, i, name):
        self.player_id = i
        self.player_name = name
        self.odai = []  # プレイヤーのお題を記録
        self.word_field = []  # 自分が場に出している文字札
        self.tokushu_card = []  # 手札に持っている特殊札
        self.amari_card = []  # 手札に持っている文字札
        self.clear = False  # 自分のパートナーのお題を当てられたかどうかを記録

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

    # Deckの末尾からcard_numの枚数分ドローする
    def draw_card(self, deck, card_num=1):
        self.card_list = []

        if len(self.cards) == 0:
            return

        # card_numの枚数だけDeckからカードをpopする
        for index in range(card_num):
            self.card_list.append(self.cards.pop())
        return self.card_list

    # 自分のカードを入れ替える
    def change_card(num_of_field, num_of_amari):
        tmp = self.word_field[num_of_field]
        self.word_field = self.amari_card[num_of_amari]
        self.amari_card[num_of_amari] = tmp

    # 特殊札をカードにつける
    def attach_tokushu(num_of_field, num_of_tokushu):
        self.word_field[num_of_field].setting_tokusyu(self.tokushu_card[num_of_tokushu].id)

    # 指定したプレイヤーと文字札を交換する
    def change_card_with_other(num_of_player, num_of_field, num_of_amari):
        target = players[num_of_player]


    def get_player():
        return self.player_id


class Game:
    def __init__(self, num_of_player, num_of_odai):
        self.num_of_player = num_of_player  # 参加するプレイヤーの人数
        self.num_of_odai = num_of_odai  # お題の文字数
        self.destroyed_card = []  # 破棄したカードのリスト

        # Deckを作成
        self.cards = []
        for i in range(47):
            self.cards.extend([Card(i), Card(i)])
        self.cards.extend([Card(47), Card(47), Card(47), Card(47), Card(47), Card(47)])
        self.cards.extend([Card(48), Card(48), Card(48)])
        self.cards.extend([Card(49), Card(49), Card(49)])
        self.cards.extend([Card(50), Card(50), Card(50), Card(50), Card(50), Card(50)])
        self.cards.extend([Card(51), Card(51), Card(51), Card(51)])
        self.cards.extend([Card(52), Card(52), Card(52), Card(52)])

        # 最後にシャッフルする
        shuffle(self.cards)


'''
    # プレイヤーの人数を決める
    def input_num_of_player():
        while True:
            num_of_player = input('プレイする人数を入力してください >> ')
            if num_of_player.isdigit():
                return num_of_player
            print('数字のみで入力してください')
        return num_of_player

    # お題の文字数を決める
    def input_num_of_odai():
        while True:
            num_of_odai = input('お題の文字数を入力してください >> ')
            if num_of_odai.isdigit():
                return num_of_odai
            print('数字のみで入力してください')
        return num_of_odai
'''

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

    # カードを配る
    def deal_card(players):
        for i in range(len(players)):





    # カードを破棄する

    # 特殊札をパートナーに渡す

    # 特殊札をパートナーからもらう

    # パートナーのお題を当てる


    def clear_check():
