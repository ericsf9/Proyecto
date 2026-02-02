---
title: ConfWS History
permalink: "/history/"
author_profile: true
sitemap: false
classes: wide
---
{% if history %}

---
{{history['History information']}}

---
<!--
Probar a despues implementar lo de meter los links de los titulos que seria tal que asi:
- [26th International Workshop on Configuration (ConfWS'24 @ CP 2024)](https://confws.github.io/2024/)
-->

{% for event in history['History events'] %}
- {{event['History event title']}}
  - {{event['History event venue']}}
<br><sub>{{event['History event content']}}.</sub>
{% endfor %}
{% endif %}