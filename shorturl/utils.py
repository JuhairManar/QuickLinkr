from random import choice
from string import ascii_letters,digits

size=7
available_chars=ascii_letters+digits
def create_random_code(chars=available_chars):
    return "".join(
        [choice(chars) for _ in range(size)]
    )

def create_shortend_url(model_instance):
    random_code=create_random_code()
    model_class=model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortend_url(model_instance)
    
    return random_code

