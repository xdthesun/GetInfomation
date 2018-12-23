# GetInfomation

#### 介绍
身份证号码和银行卡号生成工具，使用python实现

#### 软件架构
软件架构说明

#### 使用说明

一. 身份证号生成器IDNumber.py  
1. getAddressNumber(useRandom=True)  
    获取身份证地址码，传入useRandom，默认为True，表示随机生成一个地址码，否则需要输入地址后选择，地址转地址码表见addresstonumber.json  
2. getBirthdayNum(useRandom=true)  
    获取出生年月日，传入useRandom，默认为True，表示随机生成一个出生日期，否则需要输入对应的4位出生日期
3. getOrder()  
    随机生成一个顺序码  
4. getLastCode()  
    根据前17位得到最后一位校验位  
5. getIDInfo()  
    根据地址码+出生年月+顺序码+校验码得到最后的身份证号  
二. 银行卡号生成器BankCardNumber.py  
1. getBinNum(useRandom=True)  
    获取银行卡斌码，传入useRandom，默认为True，表示随机获取一个bin码，否则需要选择银行，银行名转bin码表见banknametobin.json，这里只保存了一些常见银行卡的bin码，均为6位
2. getMidNum(useRandom=True)  
    获取bin码和校验码之间的数，各个银行生成规则不同，与所要生成的银行卡位数有关，useRandom=True时，则表示生成一个16位的银行卡，则getMidNum()返回一个9位的码，否则根据输入的位数得到对应位数的银行卡  
3. getLastCode()  
    根据LHUM校验算法得到最后一位  
#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request