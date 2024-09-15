from utils.gpt.template import load_template
from utils.gpt.tcp import client

RESPONSE: str | None = None

def callback(response: str) -> None:
    global RESPONSE
    RESPONSE = response
    exit(code=0)

def ask_gpt(template_name: str, subs: dict[str, str]) -> str:
    prompt: str = load_template(name=template_name, subs=subs)
    with client(on_receive=callback, timeout=None) as clt:
        clt.send(message=prompt)
    global RESPONSE
    while True:
        if RESPONSE is not None:
            response: str = RESPONSE
            RESPONSE = None
            return response