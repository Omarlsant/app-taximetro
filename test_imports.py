# test_imports.py
def test_imports():
    try:
        import rich
        import pytest
        print("Todas las importaciones necesarias están disponibles.")
        return True
    except ImportError as e:
        print(f"Error al importar: {e}")
        return False

if __name__ == "__main__":
    test_imports()