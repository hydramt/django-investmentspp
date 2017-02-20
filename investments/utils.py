from loginbar.models import mapping
import re

def get_links(request):
    temp = request.split('/')[1:-1]
    temp2 = ['']
    for x in temp:
      temp2.append('%s/%s' % (temp2[-1], x))
    #text = temp
    hrefs = temp2[1:]
    linkdump = mapping.objects.values()
    links = []
    for x in hrefs:
        for y in linkdump:
          if re.match(y['uri'], x, re.IGNORECASE):
            temptext = y['text']
        if temptext:
          links = links + [{'uri': x, 'text': temptext}]
          temptext = ''
        else:
          links = links + [{'uri': x, 'text': x.split('/')[-1]}]
    #links = mapping.objects.values('uri','text').filter(uri__in=hrefs)
    return links
