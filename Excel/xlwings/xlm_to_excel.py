import xlwings as xw
import  xml.dom.minidom
# open xml
dom = xml.dom.minidom.parse('C:\\Users\ms\Desktop\cds.xml')

# save as excel
loss_rateFile = 'C:\\Users\\ms\\Desktop\\cds.xlsx'
wb=xw.Book(loss_rateFile) # open file 
detail_sheet=xw.Sheet("Sheet1") #sheet_name 

detail_sheet.range('A1').options(transpose=True).value= 'Name'
detail_sheet.range('B1').options(transpose=True).value = 'Type'
detail_sheet.range('C1').options(transpose=True).value= 'Value'
detail_sheet.range('D1').options(transpose=True).value = 'Unit'
detail_sheet.range('E1').options(transpose=True).value= 'Description'

#得到文档元素对象
root = dom.documentElement
itemlist = root.getElementsByTagName('Parameter')

for i in range(len(itemlist)):
    item = itemlist[i]
    itemName=item.getAttribute("name")
    detail_sheet.range('A' + str(i+2)).options(transpose=True).value= itemName
    #print (un)
    
    itemType=item.getAttribute("type")
    detail_sheet.range('B' + str(i+2)).options(transpose=True).value= itemType
    
    itemValue = item.getAttribute('value')
    detail_sheet.range('C' + str(i+2)).options(transpose=True).value= itemValue
    
    itemUnit = item.getAttribute('unit')
    detail_sheet.range('D' + str(i+2)).options(transpose=True).value= itemUnit
    
    itemDes = item.getAttribute('description')
    detail_sheet.range('E' + str(i+2)).options(transpose=True).value= itemDes
wb.save()


链接：
https://www.jb51.net/article/50812.htm
