def add_numbers(a, b):
    result = a +b
    return result
if __name__== "__main__":
    number = add_numbers(20,2)
    print(number);
# tercer ejercicio     
    """ Liberia time forma de importar una liberia """
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time} seconds")

if __name__ == "__main__":
    with Timer():  # Usando el contexto correctamente
    
        pass


#ultimo ejercicio
def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)