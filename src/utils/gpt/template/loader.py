from sys import path
from utils.gpt.template import Template

def load_template(name: str, subs: dict[str, str]) -> str:
    template_path: str = f'{path[0]}\\utils\\gpt\\prompts\\{name}.j2'
    with open(file=template_path, mode='r', encoding='UTF-8') as template_file:
        template: Template = Template(string=template_file.read())
    return template.render(subs=subs)