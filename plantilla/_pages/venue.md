---
title: Venue
permalink: "/venue/"
author_profile: true
sitemap: false
classes: wide
---
{% if venue %}

{{venue['Venue information']}}

<sub>**Venue:** {{venue['Exact location']}}
<br>{{venue['Street location']}}
</sub>
{% endif %}



