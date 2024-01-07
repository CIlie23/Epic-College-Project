from website import create_app #we can do this cause it's a python package

app = create_app()

if __name__ == '__main__': #if we run main we execute the file
    app.run(debug=True) #running web server yay, turn off in production
    