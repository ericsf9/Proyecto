---
title: Program
permalink: "/program/"
author_profile: true
sitemap: false
classes: wide
redirect_from:
- "/agenda/"
---

{{program['Program information']}}

{% for day in program['Days of the conference'] %}
|                   | *{{day['Day information']}}* |
| ------------------|----------------------------------------------------|
{% for event in day.events %}
| {{event.timelapse}}  | {{event.eventscontent}}  |
{% endfor %}


{% endfor %}

{% if program['Further program information'] %}
## {{program['Further program information']['Further program information title']}}
{{program['Further program information']['Further program information content']}}

{% endif %}