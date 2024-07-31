try:
    from functions.outputting_data import main

    if __name__ == '__main__':
        main()
except ModuleNotFoundError as e:
    print(e.msg)
except ImportError as e:
    print(e.msg.split('(')[0])
except FileNotFoundError as e:
    print(f"{e.strerror}: '{e.filename}'")
