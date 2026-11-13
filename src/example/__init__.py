"""Ejemplo mínimo: función pura con test. Sustituir por el código del producto."""


def greet(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name debe ser una cadena no vacía")
    return f"Hola, {name.strip()}!"
