import scrapy
import re

class AbreviaturasScraper(scrapy.Spider):
    name = 'AbreviaturasScraper'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_abreviaturas']

    def parse(self, response):

        for item in response.xpath('//div[@class="mw-parser-output"]/div/ul/li'):
            #print(item.xpath('./text()').extract())
            #print(item.css('a::attr(title)').extract())
            yield {
                'title': self.get_title(item),
                'abrev': self.get_abrev(item)
            }
    
    def get_abrev(self, item):
        abrev = item.xpath('./text()').extract()

        if len(abrev):
            s = abrev[0].split('—')[0].strip()
            print(s)
            return s

        return None
    
    def get_title(self, item):
        text = item.extract()

        if text:
            text = re.search(r'<li>(.+)</li>', text)
            text = text.group(1)
            try:
                title = text.split('—')[1:]
                title = '—'.join(title).strip()
            except IndexError:
                try:
                    title = text.split(' ')[1:]
                    title = ' '.join(title).strip()
                except IndexError:
                    title = text

            title_sub = re.sub(r'<a[^>]+>(.+)</a>', r'\1', title)
            title_sub = re.sub(r'(<i>)|(</i>)|(<sup.+)', '', title_sub)
            
            return title_sub

        return None