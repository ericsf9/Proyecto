---
title: Registration
permalink: "/registration/"
author_profile: true
sitemap: false
classes: wide
---

{{registration['Registration status']}}

### Registration deadlines
{% for deadline in registration['Registration deadlines'] %}
- **{{deadline['Deadline title']}}:** {{deadline['Deadline timelapse']}}
{% endfor %}

Please register at [{{registration['Registration link']}}]({{registration['Registration link']}})

{% if registration['Registration further info'] %}
### {{registration['Registration further info']['Registration further info title']}}

{{registration['Registration further info']['Registration further info content']}}
{% endif %}

### Registration fees

{{registration['Registration fees']['Registration fees info']}}

<table>
  <thead>
    <tr>
      <th>Package</th>
      {% set flag = namespace(hay_categoria=false) %}
      {% for sds in registration['Registration fees']['Registration packages'] %}
      {% if sds['Registration category'] %}
      {% set flag.hay_categoria = true %}
      {% endif %}
      {% endfor %}
      {% if flag.hay_categoria %}
      <th>Category</th>
      {% endif %}
      {% for d in registration['Registration deadlines'] %}
      <th>{{d['Deadline title']}}</th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
  {% for package in registration['Registration fees']['Registration packages'] %}
  {% if package['Registration category'] %}
  {% for category in package['Registration category'] %}
    <tr>
      {% if loop.first %}
      <td rowspan="2"><b>{{package['Package name']}}</b></td>
      {% endif %}
      <td><b>{{category['Category name']}}</b></td>
      {% for deadln in category['Registration deadlines table'] %}
      <td>{{deadln['Registration cost']}}</td>
      {% endfor %}
    </tr>
    {% endfor %}
    {% else %}
    <tr>
      <td><b>{{package['Package name']}}</b></td>
      {% for deadln in package['Registration deadlines table'] %}
      <td>{{deadln['Registration cost']}}</td>
      {% endfor %}
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
