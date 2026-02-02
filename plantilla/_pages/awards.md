---
title: Awards
permalink: "/awards/"
author_profile: true
sitemap: false
classes: wide
---

{% if awards %}
{{awards['Awards information']}}


{% for award in awards['Conference awards'] %}
- **{{award['Award title']}}**: {{award['Award content']}}.
{% endfor %}
{% endif %}