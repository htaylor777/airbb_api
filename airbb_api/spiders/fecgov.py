import scrapy
import json
from scrapy.http import Request, FormRequest


class FecgovSpider(scrapy.Spider):
    name = 'fecgov'
    allowed_domains = ['www.fec.gov']
    header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://api.open.fec.gov/v1/candidates/totals/?api_key=28Y8q8XFocq8yhKfBzzhUJXjFj2JHCZzIv4P2KIK&sort_hide_null=false&sort_nulls_last=true&election_year=2020&election_full=True&is_active_candidate=true&sort=name&per_page=30&page=1&office=H', callback=self.parse_id, headers={'User-Agent': self.header})

    def parse_id(self, response):
        data = json.loads(response.body.decode('utf-8'))
        print(data)
        with open('fec.json', 'w') as file:
            file.write(json.dumps(data))

    def parse_id(self, response):
        pass
