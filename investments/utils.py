from loginbar.models import mapping
import re

def get_links(request):
    temp = request.split('/')[1:-1]
    temp2 = ['']
    hometext=None
    for x in temp:
      temp2.append('%s/%s' % (temp2[-1], x))
    hrefs = temp2[1:]
    linkdump = mapping.objects.values('uri','text').filter(enabled=True)
    for x in linkdump:
      if x['uri'] == '/$':
        hometext = x['text']
    if hometext is None:
      hometext="Home"
    links = [{'uri': '/', 'text': hometext}]
    temptext= []
    for x in hrefs:
        for y in linkdump:
          if re.match(y['uri'], x, re.IGNORECASE):
            temptext = y['text']
        if temptext:
          links = links + [{'uri': x, 'text': temptext}]
          temptext = ''
        else:
          if x.split('/')[-1].islower():
            links = links + [{'uri': x, 'text': x.split('/')[-1].title()}]
          else:
            links = links + [{'uri': x, 'text': x.split('/')[-1] }]
    return links
