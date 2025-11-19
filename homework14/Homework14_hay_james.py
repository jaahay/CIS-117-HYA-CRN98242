from app import App

if __name__ == '__main__':
    myapp = App()
    myapp.mainloop()

# if __name__ == '__main__':
#     # Fetch and parse the page again
#     # link = 'https://collegeofsanmateo.edu/wellnesscenter'
#     link = 'https://maildiver.com/blog/mailto-links-complete-guide/'
#     from urllib.request import urlopen

#     resp = urlopen(link)
#     html = resp.read().decode().lower()

#     parser = HTMLEmailParser()
#     parser.feed(html)

#     print(parser.emails)