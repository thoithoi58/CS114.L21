from icrawler.builtin import FlickrImageCrawler
google_crawler = FlickrImageCrawler('####') #Add you Flickr here
google_crawler.crawl(group_id='14728131@N21', max_num=1000)