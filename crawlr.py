import scrapy

class RecursiveSpider(scrapy.Spider):
    name = "recursive"
    start_urls = [
        'https://en.wikipedia.org/wiki/Web_scraping',
        'https://en.wikipedia.org/wiki/Main_Page',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Scrapy',
        'https://en.wikipedia.org/wiki/General-purpose_programming_language',
        'https://en.wikipedia.org/wiki/Programming_language',
        'https://en.wikipedia.org/wiki/Software',
        'https://en.wikipedia.org/wiki/Software_development',
        'https://en.wikipedia.org/wiki/Gribov',
        'https://en.wikipedia.org/wiki/German_submarine_U-3507',
        'https://en.wikipedia.org/wiki/United_States',
        'https://en.wikipedia.org/wiki/United_States_Army',
        'https://en.wikipedia.org/wiki/United_States_Army_Air_Force',
        'https://en.wikipedia.org/wiki/United_States_Army_Air_Force_in_World_War_II',
        'https://en.wikipedia.org/wiki/United_States_Army_Air_Force_in_World_War_II#Theater_of_operations',
        'https://en.wikipedia.org/wiki/United_States_Army_Air_Force_in_World_War_II#Theater_of_operations',
        'https://en.wikipedia.org/wiki/Aki_no_Arashi',
        'https://en.wikipedia.org/wiki/Alaska',
        'https://en.wikipedia.org/wiki/Alaska_Yukon_Pacific_Exposition',
        'https://en.wikipedia.org/wiki/Alaska_Yukon_Pacific_Exposition#Exposition_buildings',
        'https://en.wikipedia.org/wiki/Diadasia',
        'https://en.wikipedia.org/wiki/Alaska_Yukon_Pacific_Exposition#Exposition_buildings',
        'https://en.wikipedia.org/wiki/Diadasia',
        'https://en.wikipedia.org/wiki/Opoczki',
        'https://en.wikipedia.org/wiki/Bucculatrix_transversella',
        'https://en.wikipedia.org/wiki/Ghana',
        'https://en.wikipedia.org/wiki/Ghanaian_cedi',
        'https://en.wikipedia.org/wiki/Kumasi',
        'https://en.wikipedia.org/wiki/Ashanti_Empire',
        'https://en.wikipedia.org/wiki/Gulf_of_Guinea',
        'https://en.wikipedia.org/wiki/Cameroon',
        'https://thejohnfox.com/2021/08/65-long-sentences-in-literature/',
        'https://learnenglish.britishcouncil.org/'
    ]
    sentence_count = 0
    max_sentences = 100000 # change this to the desired number of sentences
    scraped_data = []

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)

        for sentence in response.css('p::text').getall():
            self.sentence_count += 1
            self.scraped_data.append(sentence)
            if self.sentence_count % 1000 == 0: # show progress every 1000 sentences
                print(f'Scraped {self.sentence_count} sentences so far')
            if self.sentence_count >= self.max_sentences:
                raise CloseSpider('Reached maximum sentence count')

    def closed(self, reason):
        with open('scraped_data.txt', 'w') as f:
            for sentence in self.scraped_data:
                f.write(sentence + '\n')
