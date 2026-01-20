---
title: Awards
permalink: "/awards/"
author_profile: true
sitemap: false
classes: wide
---


{{awards['Awards information']}}

{% for award in awards['Conference awards'] %}
- **{{award['Award title']}}**: {{award['Award content']}}.
{% endfor %}