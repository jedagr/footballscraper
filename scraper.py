# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr=2017&p=.htm")
# creates an empty dictionary variable to hold data
record = {}
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
names = root.cssselect("td a")
##page_team_1_block_team_squad_8-table > tbody:nth-child(4) > tr:nth-child(3) > td:nth-child(4) > div:nth-child(1) > a
for name in names:
  #print name.text
  print name.attrib["href"]
  #store the link in the variable "record" under the key "link"
  record["link"] = name.attrib["href"]
  #record["name"] = name.text.encode("ascii", "ignore")
  print record
  #record["link"] = name.attrib["href"]
  scraperwiki.sqlite.save(unique_keys=["link"], data=record)
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
