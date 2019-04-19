import scrapy
import re


class AbreviaturasScraper(scrapy.Spider):
    name = 'AbreviaturasScraper'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_abreviaturas']

    def parse(self, response):

        for item in response.xpath('//div[@class="mw-parser-output"]/div/ul/li'):
            yield self.get_values(item.extract())

    def get_values(self, extracted_value):
        '''
            Get the abbreviations and their descriptions    

            Params:
                extracted_value(str): extracted value from the Selector object
        '''
        # extract the item's content
        text = extracted_value
        abrev = ''
        desc = ''
        result = {'abrev': '', 'desc': ''}

        if text:
            # remove the tags
            text = re.sub(
                r'(<[^>]+>)', r'', text)
            text = re.sub(r'(\[\d+\])', r'', text)

            # split the text by "—"
            splitted_text = text.split('—')

            # check if was splitted
            if len(splitted_text) >= 2:
                abrev = splitted_text[0].strip()
                desc = splitted_text[1:]
                desc = ' — '.join(desc).strip()
            else:
                # try to split by space
                splitted_text = text.split(' ')

                # check if was splitted
                if len(splitted_text) >= 2:
                    abrev = splitted_text[0].strip()
                    desc = splitted_text[1:]
                    desc = ' '.join(desc).strip()
                else:
                    abrev = text

            result['abrev'] = abrev
            result['desc'] = desc

        return result
