import omdb

client = omdb.Client(apikey="http://www.omdbapi.com/?i=tt3896198&apikey=93e1babb")# must use OMDb API parameters
res = omdb.request(t='True Grit', y=1969, r='xml')
xml_content = res.content
