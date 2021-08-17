import newspaper

url = input("Enter the URL of the Web Article: ")

url_i = newspaper.Article(url="%s" % (url), language="en")
url_i.download()
url_i.parse()


print(url_i.text)
