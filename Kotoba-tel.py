moji = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ',
        'た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む',
        'め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん','ー','濁点','半濁点',
        '小文字','確定','列確定','行確定']


class Card:
    def __init__(self, i):
        self.moji = moji[i]
        self.cardtype = cardtype_check(i)
        self.fix_type = ''

    def cardtype_check(i):
        if i < 47:
            return 'moji'
        elif i >= 47:
            return 'tokushu'

    def change_fix_type():
        print('a')

class Player:
    def __init__(self, i, name):
        self.player_id = i
        self.player_name = name
        self.word_field = []
        self.tokushu_card = []
        self.amari_card = []
        self.clear = False

class Game:
    num_of_player = 0
    num_of_char = 0
    deck = 120
    destroyed_card = []

    def clear_check():