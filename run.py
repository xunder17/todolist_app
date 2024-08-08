from app import create_app  # cannot import name 'create_app' from 'app'

app = create_app()  # Error

if __name__ == '__main__':
    app.run(debug=True) 
