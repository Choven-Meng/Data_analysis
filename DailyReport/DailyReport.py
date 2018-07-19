import pandas as pd
import numpy as np
import datetime
import xlwings as xw
import calendar
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

fileName = 'C:\\Users\\ms\\Desktop\\qb_trans_ALL\\qb_trans_ALL.xlsx'
sheet_name = 'Sheet1'
data = pd.read_excel(fileName, sheet_name=sheet_name)
# 筛选状态为成功的数据
data = data[data['状态'] == '成功']
# 今天的日期
today = datetime.date.today()


class DailyReport:

    # 获取上周日日期
    def getLastSunday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=-1)
        m1 = calendar.SUNDAY
        while today.weekday() != m1:
            today += oneday
        lastSunday = today.strftime('%Y-%m-%d')
        return datetime.datetime.strptime(lastSunday, "%Y-%m-%d").date()

    # 获取上周一日期
    def getLastMonday(self):
        lastSunday = self.getLastSunday()
        oneday = datetime.timedelta(days=-1)
        m1 = calendar.MONDAY
        while lastSunday.weekday() != m1:
            lastSunday += oneday
        lastMonday = lastSunday.strftime('%Y-%m-%d')
        return datetime.datetime.strptime(lastMonday, "%Y-%m-%d").date()

    def yesterdayInfor(self):
        """
        统计昨天数据
        :return:
        """
        # 昨天的日期
        yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
        yesterday = datetime.datetime.strptime(yesterday, "%Y-%m-%d")
        yesterday = yesterday.date()

        wb1 = xw.Book(fileName)
        detail_sheet1 = xw.Sheet("Sheet2")
        detail_sheet1.range('B1').options(transpose=True).value = '交易笔数'
        detail_sheet1.range('C1').options(transpose=True).value = '交易金额'
        detail_sheet1.range('D1').options(transpose=True).value = '交易人数'
        detail_sheet1.range('E1').options(transpose=True).value = '首次交易人数'
        detail_sheet1.range('K1').options(transpose=True).value = '交易笔数'
        detail_sheet1.range('L1').options(transpose=True).value = '交易金额'
        detail_sheet1.range('M1').options(transpose=True).value = '交易人数'
        detail_sheet1.range('N1').options(transpose=True).value = '首次交易人数'

        # 昨天统计
        yesterdayData = data[data['交易时间'].apply(lambda x: x.month == yesterday.month and x.day == yesterday.day)]
        # 获取昨天之前的数据
        yesBefor = data[data['交易时间'].apply(lambda x: (x.month == 7 and x.day < yesterday.day) or (x.month < yesterday.month))]

        for subData in yesBefor.groupby('交易类型'):
            if subData[0] == '消费':
                yesBeforUconsume = list(set(subData[1]['用户uid']))
            elif subData[0] == '提现':
                yesBeforUdraw = list(set(subData[1]['用户uid']))

        for subData in yesterdayData.groupby('交易类型'):
            if subData[0] == '消费':
                newUser = []
                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额

                for i in set(subData[1]['用户uid']):
                    if i not in yesBeforUconsume:
                        newUser.append(i)
                # 保存到表格
                detail_sheet1.range('A1').options(transpose=True).value = '消费'
                detail_sheet1.range('A2').options(transpose=True).value = '昨日:' + str(yesterday)
                detail_sheet1.range('B2').options(transpose=True).value = tradeTotal
                detail_sheet1.range('C2').options(transpose=True).value = tradeAmount
                detail_sheet1.range('D2').options(transpose=True).value = tradeNum
                detail_sheet1.range('E2').options(transpose=True).value = len(newUser)
                wb1.save()

            if subData[0] == '提现':
                newUser = []
                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额
                for i in set(subData[1]['用户uid']):
                    if i not in yesBeforUdraw:
                        newUser.append(i)

                detail_sheet1.range('J2').options(transpose=True).value = '昨日(7.16)'
                detail_sheet1.range('J1').options(transpose=True).value = '提现'
                detail_sheet1.range('K2').options(transpose=True).value = tradeTotal
                detail_sheet1.range('L2').options(transpose=True).value = tradeAmount
                detail_sheet1.range('M2').options(transpose=True).value = tradeNum
                detail_sheet1.range('N2').options(transpose=True).value = len(newUser)
                wb1.save()

    def lastWeekInfor(self):
        """
        统计上周的数据
        :return:
        """
        wb1 = xw.Book(fileName)
        detail_sheet1 = xw.Sheet("Sheet2")

        lastWeekData = data[data['交易时间'].apply(lambda x: (x.month == self.getLastSunday().month and x.day <= self.getLastSunday().day)
                                         and (x.month == self.getLastMonday().month and x.day >= self.getLastMonday().day))]
        # 获取上周之前的数据
        lastWeekBefor = data[
            data['交易时间'].apply(lambda x: (x.month == self.getLastMonday().month and x.day < self.getLastMonday().day)
                                         or (x.month < self.getLastMonday().month))]

        for subData in lastWeekBefor.groupby('交易类型'):
            if subData[0] == '消费':
                lastWeekBeforUconsume = list(set(subData[1]['用户uid']))
            elif subData[0] == '提现':
                lastWeekBeforUdraw = list(set(subData[1]['用户uid']))

        for subData in lastWeekData.groupby('交易类型'):
            if subData[0] == '消费':
                newUser = []

                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额

                for i in set(subData[1]['用户uid']):
                    if i not in lastWeekBeforUconsume:
                        newUser.append(i)



                detail_sheet1.range('A3').options(transpose=True).value = '上周:' + str(self.getLastMonday()) + '~' + str(
                    self.getLastSunday())
                detail_sheet1.range('B3').options(transpose=True).value = tradeTotal
                detail_sheet1.range('C3').options(transpose=True).value = tradeAmount
                detail_sheet1.range('D3').options(transpose=True).value = tradeNum
                detail_sheet1.range('E3').options(transpose=True).value = len(newUser)
                wb1.save()

            if subData[0] == '提现':
                newUser = []
                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额

                for i in set(subData[1]['用户uid']):
                    if i not in lastWeekBeforUdraw:
                        newUser.append(i)

                detail_sheet1.range('J3').options(transpose=True).value = '上周:' + str(self.getLastMonday()) + '~' + str(self.getLastSunday())
                detail_sheet1.range('K3').options(transpose=True).value = tradeTotal
                detail_sheet1.range('L3').options(transpose=True).value = tradeAmount
                detail_sheet1.range('M3').options(transpose=True).value = tradeNum
                detail_sheet1.range('N3').options(transpose=True).value = len(newUser)
                wb1.save()

    def historyInfor(self):
        """
        统计历史数据
        :return:
        """
        wb1 = xw.Book(fileName)
        detail_sheet1 = xw.Sheet("Sheet2")

        historyData = data[~data['交易时间'].apply(lambda x: x.month == today.month and x.day == today.day)]

        for subData in historyData.groupby('交易类型'):
            if subData[0] == '消费':
                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额
                detail_sheet1.range('A4').options(transpose=True).value = '历史信息<' + str(today)
                detail_sheet1.range('B4').options(transpose=True).value = tradeTotal
                detail_sheet1.range('C4').options(transpose=True).value = tradeAmount
                detail_sheet1.range('D4').options(transpose=True).value = tradeNum
                wb1.save()

            if subData[0] == '提现':
                tradeTotal = len(subData[1]['交易订单ID'])  # 交易笔数
                tradeNum = len(set(subData[1]['用户uid']))  # 人数
                tradeAmount = subData[1]['交易金额'].sum()  # 交易金额
                detail_sheet1.range('J4').options(transpose=True).value = '历史信息<' + str(today)
                detail_sheet1.range('K4').options(transpose=True).value = tradeTotal
                detail_sheet1.range('L4').options(transpose=True).value = tradeAmount
                detail_sheet1.range('M4').options(transpose=True).value = tradeNum

                wb1.save()

    def plot(self):
        """
        绘制图
        :return:
        """
        # 转换时间变成年月日格式
        data['交易时间'] = data['交易时间'].apply(lambda x: datetime.datetime.strptime(x.strftime("%Y-%m-%d"), "%Y-%m-%d"))
        for subData in data.groupby('交易类型'):
            # 消费数据集
            if subData[0] == '消费':
                consumeData = subData[1]
                dateTime = []
                consumeCount = []  # 消费人数
                consumeTotal = []  # 消费笔数
                consumeRate = []  # 消费均额
                # 消费
                for i, j in consumeData.groupby('交易时间'):
                    dateTime.append(i)
                    consumeCount.append(len(set(j['用户uid'])))
                    consumeTotal.append(len(j['交易订单ID']))
                    consumeRate.append(sum(j['交易金额'] / len(j['交易订单ID'])))
                # 绘制消费数据
                fig = plt.figure(figsize=(10, 9))
                ax1 = fig.add_subplot(211)

                plt.plot(dateTime, consumeCount, marker='o', mec='r', mfc='w', label='消费人数')
                plt.plot(dateTime, consumeTotal, marker='*', ms=10, label='消费笔数')
                plt.legend(loc='upper left')  # 让图例生效
                plt.margins(0)
                plt.subplots_adjust(bottom=0.15)
                plt.xlabel("日 期", fontsize=10)  # X轴标签，字体大小
                fig.autofmt_xdate(rotation=30)  # x轴标签倾斜30度

                plt.ylabel("数 量", fontsize=15)  # Y轴标签
                plt.ylim((0, 40))  # 范围
                plt.yticks(np.arange(0, 40, 2)) # y轴刻度
                plt.title("统计消费数据", fontsize=18, color='r')  # 标题
                # 绘制笔均额
                ax2 = fig.add_subplot(212)
                plt.plot(dateTime, consumeRate, label='笔均')
                plt.legend(loc='upper left')
                plt.subplots_adjust(bottom=0.15)
                plt.xlabel("日 期", fontsize=15)  # X轴标签
                plt.ylabel("平均每笔消费", fontsize=15)  # Y轴标签
                fig.autofmt_xdate(rotation=30)

                plt.show()

            # 提现数据集
            if subData[0] == '提现':
                drawData = subData[1]
                drawDateTime = []
                drawCount = []  # 提现人数
                drawTotal = []  # 提现笔数
                drawRate = []
                for i, j in drawData.groupby('交易时间'):
                    drawDateTime.append(i)
                    drawCount.append(len(set(j['用户uid'])))
                    drawTotal.append(len(j['交易订单ID']))
                    drawRate.append(sum(j['交易金额'] / len(j['交易订单ID'])))

                fig = plt.figure(figsize=(10, 9))
                ax1 = fig.add_subplot(211)
                plt.plot(drawDateTime, drawCount, marker='o', mec='r', mfc='w', label='提现人数')
                plt.plot(drawDateTime, drawTotal, marker='*', ms=10, label='提现笔数')
                plt.legend(loc='upper left')  # 让图例生效
                plt.margins(0)
                plt.subplots_adjust(bottom=0.15)
                # plt.xlabel("日 期",fontsize=10) #X轴标签
                plt.ylabel("数 量", fontsize=15)  # Y轴标签
                plt.ylim((0, 18))
                plt.yticks(np.arange(0, 18, 1))
                plt.title("统计提现数据", fontsize=18, color='r')  # 标题
                fig.autofmt_xdate(rotation=30)

                ax2 = fig.add_subplot(212)
                plt.plot(drawDateTime, drawRate, marker='+', mec='k', mfc='w', label='提现笔均')
                plt.legend(loc='upper left')
                plt.subplots_adjust(bottom=0.15)
                plt.xlabel("日 期", fontsize=15)  # X轴标签
                # plt.xticks(np.array(drawDateTime))
                plt.ylabel("平均每笔提现", fontsize=15)  # Y轴标签
                fig.autofmt_xdate(rotation=30)
                plt.show()

if __name__ == '__main__':
    #DailyReport().yesterdayInfor()
    #print(DailyReport().getLastSunday())
    #DailyReport().lastWeekInfor()
    #DailyReport().historyInfor()
    DailyReport().plot()