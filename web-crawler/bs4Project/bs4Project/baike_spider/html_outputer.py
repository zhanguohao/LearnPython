# -*- coding: utf-8 -*-


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        with open('output.html', 'w') as out:
            out.write('<html>')
            out.write('<body>')
            out.write('<table>')
            for data in self.datas:
                out.write('<tr>')
                out.write('<td>%s</td>' % data['url'].encode('utf-8'))
                out.write('<td>%s</td>' % data['title'].encode('utf-8'))
                out.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                out.write('</tr>')
            out.write('</table>')
            out.write('</body>')
            out.write('</html>')
