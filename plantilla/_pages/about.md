---
title: '{{home['Conference name']}}<br><span style="font-size: 60%;">{{home['Conference venue']}}. {{home['Conference date']}}</span>'
permalink: "/"
header:
  overlay_image: '{{home.headerimage}}'
  overlay_filter: 0.3
  caption: '[Bologna, Italy](https://www.bolognawelcome.com/en/blog/top-10-things-to-do-in-bologna-)'
author_profile: true
classes: wide
redirect_from:
- "/about/"
- "/about.html"
---


<!--
AQUI ANTES ESTABA ABIERTO EL LINK PARA EL REGISTRO EN LA PAGINA PRINCIPAL PODEMOS VERLO PARA METER MAS VARIABILIDAD, O ALOMEJOR ES DEMASIADO PORQUE ESO DEPENDERIA DEL MOMENTO EN EL QUE SE HABRAN LOS REGISTROS

# [Registration](https://confws.github.io/registration/) is open now.
-->

**{{home['Conference name']}}**

<img style="float: right; width: 400px;" src="{{home.logoimage}}">

---
- {{home['Conference date']}}
- {{home['Conference venue']}}
- Format: {{home['Conference format']}}

{% if home['Short name for the conference'] %}
# {{home['Short name for the conference']}} aims
{% else %}
# {{home['Conference name']}} aims
{% endif %}
{{home.aims.aimscontent}}


---

<!--
CAMBIAR ESTO Y METERLO EN VARIABILIDAD
-->

![ConfWS will be at Bologna](assets/confws/bg_bologna.jpg "ConfWS will be at Bologna")

