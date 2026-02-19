# PRNG(메르센 트위스터) -> CSPRNG(OS 엔트로피) 방식으로 교체  
# 사실상 예측 불가능, 예측하면 개고수  

# 베팅
def betpoint(uid,point):
    if uid not in userdata:
        newdata(uid)
    if point < 1:
        return [False,'올바른 정수를 입력해주세요.']
    if userdata[uid]['points'] < point:
        return [False,'돌멩이가 부족합니다.\n현재 돌멩이 : '+formatpoint(userdata[uid]['points'])]
    userdata[uid]['bettry'] += 1
    ran = secrets.randbelow(100) + 1
    if ran >= 50:
        userdata[uid]['betwon'] += 1
        if ran > 95:
            addpoint(uid,point*2,'bet wx2')
            ebd = Embed(title="베팅 2배 성공!", description="현재 돌멩이 : "+formatpoint(userdata[uid]['points']), color=0x00ff00)
            return [True,ebd]
        else:
            addpoint(uid,point,'bet w')
            ebd = Embed(title="베팅 성공!", description="현재 돌멩이 : "+formatpoint(userdata[uid]['points']), color=0x00ff00)
            return [True,ebd]
    else:
        addpoint(uid,-point,'bet L')
        ebd = Embed(title="베팅 실패!", description="현재 돌멩이 : "+formatpoint(userdata[uid]['points']), color=0xff0000)
        return [True,ebd]


# 슬롯머신
SYMBOLS = ["🍒", "🔔", "💎"] 
WEIGHTS = [10, 10, 7]
WEIGHTED_SYMBOLS = []
for symbol, weight in zip(SYMBOLS, WEIGHTS):
    WEIGHTED_SYMBOLS.extend([symbol] * weight)
def reelslot():
    reel = []
    for _ in range(ROWS):
        row = [secrets.choice(WEIGHTED_SYMBOLS) for _ in range(COLS)]
        reel.append(row)
    return reel

# 카드 덱
def secureshuffle(items):
    n = len(items)
    for i in range(n - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        items[i], items[j] = items[j], items[i]
    return items
class Deck:
    def __init__(self):
        self.cards = []
        self._build()
    def _build(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['S', 'H', 'D', 'C']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        secureshuffle(self.cards)
    def deal(self) -> Card:
        if not self.cards:
            self._build()
        return self.cards.pop()
      
