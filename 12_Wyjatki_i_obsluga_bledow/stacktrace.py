from my_package import functions
import traceback

if __name__ == '__main__': #tutaj glowny kod programu
    try:
        functions.ok_function() #cala logika mieszka w ok function (pakiet poznajemy po init)
    except IndexError as e:
        print(e)
        print(traceback.format_exc())
    except Exception as e:
        print(e)

