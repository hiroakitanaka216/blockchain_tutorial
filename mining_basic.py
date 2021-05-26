import hashlib
import random
import string

class Mining():
    def __init__(self,difficulty):
        self.data = self.calcRandomText(10) #データ
        self.difficulty = difficulty #求める規定のハッシュ値の難易度(何文字か)
        self.nonce = 0 #ナンス
        self.answerText = self.calcRandomHexDigitsText(self.difficulty) #求める規定のハッシュ値を算出
        self.nonceDataText = self.calcNonceDataText() #データとナンス値を合わせる
        self.hashText = self.calcHash(self.nonceDataText) #ハッシュ値を算出する

        self.miningLoop() #マイニング開始

    def calcRandomText(self,num): #ランダムな文字列を返す
        _randTextList = [random.choice(string.ascii_letters + string.digits) for i in range(num)]
        return "".join(_randTextList)

    def calcRandomHexDigitsText(self,num): #16進数のランダムな文字列を返す
        _randHexDigitsTextList = [random.choice(string.hexdigits) for i in range(num)]
        return "".join(_randHexDigitsTextList)

    def calcNonceDataText(self): #データのナンス値を合わせる
        return self.data + str(self.nonce)

    def calcHash(self,text): #ハッシュ値を算出する
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def miningLoop(self): #マイニングのメソッド
        while self.hashText[-1*self.difficulty:] != self.answerText.lower():
            print("マイニング中  試行回数:" + str(self.nonce+1) + "  求める規定のハッシュ値:"+ self.answerText.lower() + "  算出ハッシュ値:" + self.hashText[-1*self.difficulty:])
            self.nonce += 1 #ナンス値に1を加算していく
            self.nonceDataText = self.calcNonceDataText() #データとナンス値を合わせる
            self.hashText = self.calcHash(self.nonceDataText) #ハッシュ値を算出する
        print("マイニング中  試行回数:" + str(self.nonce+1) + "  求める規定のハッシュ値:"+ self.answerText.lower() + "  算出ハッシュ値:" + self.hashText[-1*self.difficulty:] + "\n")

        print("マイニング成功!" + "  データ:" + self.data + "  ナンス値:" + str(self.nonce))
        print("マイニングに成功したハッシュ値:" + self.calcHash(self.data + str(self.nonce)))

def main():
    difficulty = 3 #求める規定のハッシュ値の難易度(何文字か)
    mining = Mining(difficulty) #インスタンスの生成

if __name__ == "__main__":
    main()
