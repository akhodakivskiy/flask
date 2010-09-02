from accounts import module

@module.route('/')
def index():
    return "Hello World!" 
