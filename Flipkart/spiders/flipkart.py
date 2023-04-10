import scrapy

class FlipkartSpider(scrapy.Spider):
    name="flipkart"
    start_urls=["https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=5f976449-c4b9-4cb6-84b1-6e87b12afb81&as-backfill=on"]
    
    def parse(self, response):
        phone=response.css("._4rR01T::text").extract()
        price=response.css("._1_WHN1::text").extract() 
        ratings=response.css("._3LWZlK::text").extract()
        description=response.css(".rgWa7D::text").extract() 
        yield {'Phones':phone,'Price':price,'Ratings':ratings,'Description':description}