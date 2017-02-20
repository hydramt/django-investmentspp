from loginbar.models import mapping

def get_links(request):
    temp = request.split('/')[1:-1]
    temp2 = ['']
    for x in temp:
      temp2.append('%s/%s' % (temp2[-1], x))
    #text = temp
    hrefs = temp2[1:]
    links = mapping.objects.values('uri','text').filter(uri__in=hrefs)
    return links
