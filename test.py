from function.BankCardNumber import GetBankCardNumber

test = GetBankCardNumber()

# print(test.getBankCardNumber(useRandom=False))
# print(str(reversed("625965087177209")))
print("最后一位结果：", test.getLastcode("622609355837957"))
