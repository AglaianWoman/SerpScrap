#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pprint
import serpscrap


def scrape(config, keywords):
    scrap = serpscrap.SerpScrap()
    scrap.init(config=config.get(), keywords=keywords)
    return scrap.run()


def scrape_to_csv(config, keywords):
    scrap = serpscrap.SerpScrap()
    scrap.init(config=config.get(), keywords=keywords)
    return scrap.as_csv('/tmp/output')


def get_related(results, related):
    for result in results:
        if 'related_keywords' in result.keys():
            for keyword in result['related_keywords']:
                if keyword['keyword'] not in related:
                    related.append(keyword['keyword'])
    return related


config = serpscrap.Config()
config.set('scrape_urls', False)
keywords = ['new york']
related = []
related = get_related(scrape(config, keywords), related)
related = get_related(scrape(config, related), related)
# related = get_related(scrape(config, related), related)
scrape_to_csv(config, related)

pprint.pprint('********************')
pprint.pprint(related)
