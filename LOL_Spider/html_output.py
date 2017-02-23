# -*- coding:utf-8 -*-
# 最后的结果输出
# 提供两个功能，一个事收集数据，另一个是输出数据
import db_output

class Outputer(object):
    # 收集数据需要一个列表list进行维护
    def __init__(self):
        self.datas= []
        self.db = db_output.DatabaseOutputer()

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出一个html文档
    def output_html(self):
        fileout = open("output.html", "w")
        fileout.write("<html>")
        fileout.write("<head>")
        fileout.write("<meta charset=\'utf-8\'>")
        fileout.write("</head>")
        fileout.write("<body>")
        fileout.write("<table>")
        for data in self.datas:
            fileout.write("<tr>")
            fileout.write("<td>%s</td>" % data['url'])
            fileout.write("<td>%s</td>" % data['champion_name'].encode('utf-8'))
            fileout.write("<td>%s</td>" % data['nick_name'].encode('utf-8'))
            fileout.write("<td>%s</td>" % str(data['abilities']))
            fileout.write("</tr>")
        fileout.write("</table>")
        fileout.write("</body>")
        fileout.write("</html>")
        fileout.close()

    def save_to_db(self):
        table = self.db.creatTable('LOL_Crawler')
        for data in self.datas:
            url = data['url']
            champion_name = data['champion_name']
            nick_name = data['nick_name']
            abilities = data['abilities']
            haha = ""
            for ability in abilities:
                 haha = haha + ability + ' '
            self.db.inserttable(table, url, champion_name, nick_name, haha)
