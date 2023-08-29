from routes import create_app
# from service.pos_code import PokaYokeSystem
# import threading

if __name__ == '__main__':
    # t1 = threading.Thread(target=PokaYokeSystem)
    # t1.start()
    app = create_app()
    app.run(debug=True)
    # t1.join()
    