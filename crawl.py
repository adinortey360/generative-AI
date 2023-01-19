import scrapy
import wikipedia

class SentenceSpider(scrapy.Spider):
    name = "sentences"
    start_urls = [
        'https://en.wikipedia.org/wiki/Web_scraping',
    ]

    count = 0
    for i in range(20):
        try:
            page = wikipedia.random()
            start_urls.append(wikipedia.page(page).url)

            print(count)
            print(wikipedia.page(page).url)
            count += 1
        except:
            continue


    sentence_count = 0
    max_sentences = 500000 # change this to the desired number of sentences
    scraped_sentences = []

    def parse(self, response):
        for sentence in response.css('p::text').getall():
            self.sentence_count += 1
            self.scraped_sentences.append(sentence)
            if self.sentence_count >= self.max_sentences:
                break
        next_page = response.css('a::attr(href)').get()
        if next_page is not None and self.sentence_count < self.max_sentences:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        with open('scraped_sentences.txt', 'w') as f:
            for sentence in self.scraped_sentences:
                f.write(sentence + '\n')
