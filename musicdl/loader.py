from .musicdl import musicdl

config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': 3, 'proxies': {}}
# target_srcs = [
#     'baiduFlac', 'kugou', 'kuwo', 'qq', 'qianqian',
#     'netease', 'migu', 'xiami', 'joox', 'yiting',
# ]

target_srcs = [
     'kugou', 'qq', 'qianqian', 'migu', 'xiami', 'joox', 'yiting',
]

client = musicdl(config=config)
client.run(target_srcs)