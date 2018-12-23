from function import IDNumber, BankCardNumber


if __name__ == '__main__':
    print("------身份证&银行卡号生成器------")
    print('''请输入对应指令（默认随机生成一个身份证和16位银行卡）：
            0.随机生成一个身份证号和银行卡号
            1.生成一个身份证号
            2.生成一个银行卡号''')
    print("------------------------------")
    idNumber = IDNumber.GetIDNumber()
    bankCardNumber = BankCardNumber.GetBankCardNumber()
    x = input("请输入指令：")
    if len(x) == 0 or int(x) == 0:
        print("身份证号：%s" % idNumber.getIDInfo())
        print("银行卡号：%s" % bankCardNumber.getBankCardNumber())
    elif int(x) == 1:
        print('''
        输入以下指令（默认为随机生成一个身份证号）：
            1.随机生成一个身份证号
            2.指定地址和生日''')
        y = input("请输入指令：")
        if len(y) == 0 or int(y) == 1:
            print(idNumber.getIDInfo())
        else:
            print(idNumber.getIDInfo(useRandom=False))
    else:
        print('''
        输入以下指令（默认为随机生成一个银行卡号）：
            1.随机生成一个银行卡号
            2.指定银行和位数''')
        y = input("请输入指令：")
        if len(y) == 0 or int(y) == 1:
            print(bankCardNumber.getBankCardNumber())
        else:
            print(bankCardNumber.getBankCardNumber(useRandom=False))
