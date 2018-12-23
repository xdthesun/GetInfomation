import random
import json


class GetBankCardNumber(object):
    def __init__(self):
        self.binNum = ""
        self.midNum = ""
        self.lastCode = ""
        self.bankCardNumber = ""

    def getBinNum(self, useRandom=True):
        bankToBin = json.load(open("function/json/banknametobin.json", encoding="utf-8"))
        if useRandom:
            print("随机生成一个银行bin号......")
            tempBank = random.sample(bankToBin.keys(), 1)[0]
            self.binNum = bankToBin[tempBank]
            return self.binNum, tempBank
        else:
            print("请选择银行：")
            bankList = list(bankToBin.keys())
            for i in range(len(bankList)):
                print("%d.%s" % (i, bankList[i]))
            bankNum = input()
            if len(bankNum) == 0:
                return self.getBinNum()
            elif int(bankNum) in range(len(bankList)):
                self.binNum = bankToBin[bankList[int(bankNum)]]
                return self.binNum, bankList[int(bankNum)]
            else:
                print("输入有误，请重新输入:")
                return self.getBinNum(useRandom=False)

    def getMidNum(self, useRandom=True):
        if useRandom:
            print("默认生成一个16位的银行卡")
            tempMidnum = ""
            for x in range(9):
                tempMidnum = tempMidnum + str(random.randint(0, 10))
                x = x
            self.midNum = tempMidnum
            return self.midNum
        else:
            tempNum = input("请输入要生成银行卡位数（16或19位）：")
            if len(tempNum) == 0:
                return self.getMidNum()
            elif int(tempNum) in (16, 19):
                tempMidnum = ""
                for x in range(int(tempNum)-6-1):
                    tempMidnum = tempMidnum + str(random.randint(0, 10))
                self.midNum = tempMidnum
                return self.midNum
            else:
                print("输入有误，请重新输入:")
                return self.getMidNum(useRandom=False)

    def getLastcode(self, bankNumNoLastcode):
        sum = 0
        for i in bankNumNoLastcode[-1::-2]:
            for m in str(int(i)*2):
                sum = sum + int(m)
        for j in bankNumNoLastcode[-2::-2]:
            sum = sum + int(j)
        if sum % 10 == 0:
            self.lastCode = '0'
        else:
            self.lastCode = str(10 - sum % 10)
        return self.lastCode

    def getBankCardNumber(self, useRandom=True):
        if useRandom:
            self.getBinNum()
            self.getMidNum()
        else:
            self.getBinNum(useRandom=False)
            self.getMidNum(useRandom=False)
        self.getLastcode(self.binNum + self.midNum)
        self.bankCardNumber = self.binNum + self.midNum + self.lastCode
        return self.bankCardNumber
