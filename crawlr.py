import scrapy

class MediumSentencesSpider(scrapy.Spider):
    name = "medium_sentences"
    start_urls = ["https://medium.com/"]

    count = 0
    max_sentences = 20000

    def parse(self, response):
        for sentence in response.xpath("//p/text()").getall():
            self.count += 1
            yield {"sentence": sentence}
            if self.count >= self.max_sentences:
                self.crawler.engine.close_spider(self, 'Sentences limit reached')
                break

process = scrapy.crawler.CrawlerProcess()
process.crawl(MediumSentencesSpider)
process.start()
process.join()

with open('scraped_sentences.txt', 'w') as f:
    for sentence in MediumSentencesSpider.sentences:
        f.write(sentence)
        f.write("\n")