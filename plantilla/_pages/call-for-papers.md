---
title: Call for Papers
permalink: "/call-for-papers/"
author_profile: true
classes: wide
redirect_from:
- "/call-for-papers/"
---

| Important dates                              |
| -------------------- | --------------------- |
{% for importantdate in callforpapers.cimportantdates %}
| {{importantdate.description}}   | {{importantdate.cdate}}|
{% endfor %}


{% for section in callforpapers.sections %}
## {{section.sectitle}}
{{section.seccontent}}

{% for subsection in section.subsections %}
- **{{subsection.subsectitle}}** {{subsection.subseccontent}}
{% endfor %}

{{section.seccontentp}}
{% endfor %}

<!--
Tenemos esta linea despues del contenido de las subsecciones (puntos) ver afecta a algo importante y ponerlo entonces
{: .text-justify}
-->
