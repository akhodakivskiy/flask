from admin import module

@module.route('/admin/')
def index():
    return "Hello Admin World!" 
