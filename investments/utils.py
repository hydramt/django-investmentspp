def get_links(request):
    temp = request.split('/')[1:-1]
    #x=1
    #hrefs = List()
    #text = []
    #for i in temp:
    #  temp2 = []
    #  for y in i:
    #    temp2 = temp2.append(y)
    #  hrefs = hrefs + [ '/'.join(temp2) ]
    #  text = text.append(i)
    #links = {'hrefs': hrefs, 'text': text}
    temp2 = ['']
    for x in temp:
      temp2.append('%s/%s' % (temp2[-1], x))
    text = temp
    hrefs = temp2[1:]
    links = zip(text, hrefs)
    return links
