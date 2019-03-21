from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
# 1.tao ket noi
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
# 1.1 tai trang web ve
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
# with open("cafe.html","wb") as f:
#     f.write(raw_data)
soup = BeautifulSoup(html_content,"html.parser")
table = soup.find("table",id = "tableContent")
tr_list = table.find_all("tr")
ls=[]
for tr in tr_list:
        td_list =tr.find_all("td")
        dic = {}
        for i in range(len(td_list)):
                if td_list[i].string != None:
                        if i ==0:
                                dic["danh muc"]=td_list[i].string.strip()
                        elif i ==1:
                                dic["quy 4 nam 2016"]=td_list[i].string.strip()
                        elif i ==2:
                                dic["quy 1 nam 2017"]=td_list[i].string.strip()
                        elif i ==3:
                                dic["quy 2 nam 2017"]=td_list[i].string.strip()
                        elif i ==4:
                                dic["quy 3 nam 2017"]=td_list[i].string.strip()
        if dic != {}:
                ls.append(dic)
pyexcel.save_as(records=ls, dest_file_name="cafe.xlsx")





