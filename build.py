import json
from jinja2 import Environment, FileSystemLoader

with open("data.json") as f:
    data = json.load(f)

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=True,
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template("template.html")
html = template.render(**data)

with open("docs/index.html", "w") as f:
    f.write(html)

print("Built index.html")
