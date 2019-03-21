
from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=SiAuAJBZuGs']) 



# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=kImpWphugRY', 'https://www.youtube.com/watch?v=LspZCNNP6aE'])



# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=2nqIAOU34jI'])




# options = {
#     'default_search': 'ytsearch', 
# }
# dl = YoutubeDL(options)
# dl.download(['forever love viet Underground'])



options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['so far binz'])