---
title: Committees
permalink: "/committees/"
author_profile: true
classes: wide
redirect_from:
- "/organizers/"
---
{% if committees %}

## Workshop Chairs
{% for chair in committees['Workshop chairs'] %}
* {{chair['Workshop chair content']}}
{% endfor %}


## Program Committee
{% for chair2 in committees['Program committee'] %}
* {{chair2['Program chair content']}}
{% endfor %}

{% for comite in committees['Other committees'] %}
## {{comite['Committee title']}}
{% for chair3 in comite['Committee chairs'] %}
* {{chair3['Committee content']}}
{% endfor %}
{% endfor %}
{% endif %}