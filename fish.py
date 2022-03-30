import requests
from bs4 import BeautifulSoup as bs
import csv

new = []


r = requests.get("https://stardewvalleywiki.com/Fish")
fish = bs(r.content, "html.parser")

# Headers for each categorey
a = fish.select("table:nth-of-type(1) th")
title = [z.text.strip() for z in a]


Headers = [title[1], title[6], title[7], title[8], title[9], title[13]]

# Name of each fish
b = fish.select("table:nth-of-type(1) tr td:nth-of-type(2) a[title]:nth-of-type(1)")
name = [y.text.strip() for y in b]

# Locations
c = fish.select("table:nth-of-type(1) tr td:nth-of-type(7)")
location = [x.text.strip() for x in c]

# Times
d = fish.select("table:nth-of-type(1) tr td:nth-of-type(8)")
time = [w.text.strip().replace(u"\xa0", "") for w in d]

# Seasons
e = fish.select("table:nth-of-type(1) tr td:nth-of-type(9)")
season = [v.text.strip().replace(u"\xa0", ", ") for v in e]

# Weather
f = fish.select("table:nth-of-type(1) tr td:nth-of-type(10)")
weather = [u.text.strip().replace(u"\xa0", ", ") for u in f]

# What each fish can be used in
g = fish.select('table:nth-of-type(1) tr td:nth-of-type(14)')
use = ["" if t.find(title="Bundles") is None else t.find(title="Bundles").text for t in g]


with open("StardewFish.csv", "w", newline='') as file:
    write = csv.writer(file)

    data = list(zip(name, location, time, season, weather, use))
    data.insert(0, Headers)

    for row in data:
        row = list(row)
        write.writerow(row)

