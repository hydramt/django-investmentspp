def get_links(request):
    temp = request.split('/')[1:-1]
    temp2 = ['']
    for x in temp:
      temp2.append('%s/%s' % (temp2[-1], x))
    text = temp
    hrefs = temp2[1:]
    links = zip(text, hrefs)
    return links
