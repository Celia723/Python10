import functools
import time
from typing import Any, Callable


def spell_timer(func: Callable)-> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        inicio = time.time()

        resultado = func(*args, **kwargs)

        fin = time.time()

        tiempo_total = fin - inicio
        print(f"Spell completed in {tiempo_total:.3f} seconds")

        return resultado
        
    return wrapper


def power_validator(min_power: int)-> Callable:
    def need_fun(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
           
            power = args[-1] if args else 0

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return need_fun


def retry_spell(max_attempts: int)-> Callable:
    def need_fun(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for n in max_attempts:
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print("you have an other try")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return need_fun


class MageGuild():

    @staticmethod
    def validate_mage_name(name: str)-> bool:
        if len(name) < 3:
            return False
        
        return name.replace(" ", "").isalpha()
    
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int)-> str:
        return f"Successfully cast {spell_name} with {power} power"
