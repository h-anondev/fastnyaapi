from NyaaPy import sukebei

javtitle = "JUFE-174"
nyaa = sukebei.SukebeiNyaa()
results = nyaa.search(javtitle, category=2, filters=0)
print(results)