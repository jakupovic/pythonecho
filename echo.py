import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

    def POST(self, name):
	data = web.data() # you can get data use this method
	print data
	return "hello"

if __name__ == "__main__":
    app.run()


