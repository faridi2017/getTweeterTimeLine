import twitter
import pprint

consumer_key="Czj9uan8Y8YmBeNOcOYHjXhrz"
consumer_secret="94jYWEvT8ORWYz2IR2oFTcC0YFkxTPNLiESI1GpPCoREYwa9SN"
access_token="1090473564287848448-8RmKIzWHt8CoZ7PC46oLli53UpaDYH"
access_token_secret="OhwNSGhUa4jUdrqepZBcx1pNYPgRPUdraVtSC79zJH97m"

t = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_token_secret)
results = t.GetSearch(raw_query="q=from%3Afaridi56888245&src=typd")

pprint.pprint (results)
print('=============================================')
results1 = t.GetSearch(
    raw_query="q=twitter%40ShashiTharoor&result_type=recent&count=4")

pprint.pprint(results1)

'''
faridi56888245
ArvindKejriwal
ShashiTharoor,
cricdrugs
'''