import random
import time
import json


class GetIDNumber(object):
    def __init__(self):
        self.addressNum = ''
        self.birthdayNum = ''
        self.orderNum = ''
        self.lastCode = ''
        self.idInfo = ''

    def getAddressNum(self, useRandom=True):
        # 存储地址和地址码之间的对应
        addressToNumber = json.load(open("function/json/addresstonumber.json", encoding="utf-8"))
        # 随机生成一个地址码
        if useRandom:
            print("随机生成一个地址码.....")
            tempAddress = random.sample(list(addressToNumber.keys()), 1)[0]
            self.addressNum = addressToNumber[tempAddress]
            return self.addressNum, tempAddress
        # 根据用户提供的信息
        else:
            address = input("请输入省份或城市：\n")
            tempList = []
            if len(address) == 0:
                return self.getAddressNum(useRandom=False)
            for x in addressToNumber.keys():
                if address in x:
                    tempList.append(x)
            if len(tempList) == 0:
                print("输入的省份或城市未找打，请确认！")
                return self.getAddressNum(useRandom=False)
            print("请选择对应的城市:")
            for i in range(len(tempList)):
                print(str(i) + "." + tempList[i])
            num = input("请输入对应城市编号（默认则为随机选择以下任意一个城市）:")
            if len(num) == 0:
                num = random.randint(0, len(tempList))
            else:
                num = int(num)
            tempNumber = addressToNumber[tempList[num]]
            self.addressNum = tempNumber
            return tempNumber, tempList[int(num)]

    def getBirthdayNum(self, useRandom=True):
        # 随机生成一个年月日
        if useRandom:
            print("随机生成一个出生日期......")
            startTime = int(time.mktime((1984, 1, 1, 0, 0, 0, 0, 0, 0)))
            endTime = int(time.time())
            x = random.randrange(startTime, endTime)
            date_touple = time.localtime(x)
            date = time.strftime("%Y%m%d", date_touple)
            self.birthdayNum = date
            return date
        # 根据用户提供的信息
        else:
            birthday = input("请输8位生日（格式xxxxxxxx，如19930405）：")
            if len(birthday) == 0:
                self.birthdayNum = self.getBirthdayNum()
                return self.birthdayNum
            elif len(birthday) != 8:
                print("输入有误！")
                self.birthdayNum = self.getBirthdayNum(useRandom=False)
                return self.birthdayNum
            else:
                self.birthdayNum = birthday
                return self.birthdayNum

    def getOrder(self):
        temp = random.randint(0, 999)
        if temp < 10:
            self.orderNum = '00' + str(temp)
            return self.orderNum
        elif temp < 100:
            self.orderNum = '0' + str(temp)
            return self.orderNum
        else:
            self.orderNum = str(temp)
            return self.orderNum

    def getLastCode(self, top17=''):
        # 加权因子
        factorNumber = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        if len(top17) == 0:
            temp = self.addressNum + self.birthdayNum + self.orderNum
        else:
            temp = top17
        lastcodetemp = 0
        for i, j in zip(factorNumber, temp):
            lastcodetemp = lastcodetemp + i * int(j)
        lastcodetemp = 12 - lastcodetemp
        lastcode = 'X' if lastcodetemp % 11 == 10 else lastcodetemp % 11
        self.lastCode = str(lastcode)
        return lastcode

    def getIDInfo(self, useRandom=True):
        if useRandom:
            self.getAddressNum()
            self.getBirthdayNum()
        else:
            self.getAddressNum(useRandom=False)
            self.getBirthdayNum(useRandom=False)
        self.getOrder()
        self.getLastCode()
        self.idInfo = self.addressNum + self.birthdayNum + self.orderNum + self.lastCode
        return self.idInfo
