import web 

urls = [
        '/', 'Home',
        '/info','Info',
        '/home','Home',
        '/download','Download',
        '/rankings','Rankings',
        '/vote','Vote',
        '/donate','Donate',
        '/forum','Forum',
        '/register','Register',
        '/login','Login'
]   

app = web.application(urls, globals(), autoreload=True)
web.config.debug = True

class Home:
    def __init__(self):
        self.render = web.template.render('templates/' , base = 'base')
    
    def GET(self):
        return self.render.info("Home")

class Info:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Info")

class Download:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Download")

class Rankings:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Rankings")

class Vote:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Vote")

class Donate:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Donate")

class Forum:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Forum")

class Register:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Register")

class Login:

    def __init__(self):
        self.render = web.template.render('templates/', base = 'base')

    def GET(self):
        return self.render.info("Login")


if __name__ == "__main__":
    app.run()