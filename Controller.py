import web
from Models import RegisterModel

# Routes
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


# Classes
class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_input = RegisterModel.RegisterModel
        reg_input.insert_user(data)
        return data


if __name__ == "__main__":
    app.run()
