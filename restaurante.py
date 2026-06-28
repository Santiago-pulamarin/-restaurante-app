# Servicio principal que gestiona productos y clientes del restaurante
# Actúa como el núcleo administrativo del sistema

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Gestiona el catálogo de productos y la base de clientes del restaurante."""

    def __init__(self, nombre: str, direccion: str) -> None:
        # Nombre oficial del restaurante
        self.nombre: str = nombre
        # Dirección física del local
        self.direccion: str = direccion
        # Lista de productos registrados en el sistema
        self.productos: list[Producto] = []
        # Lista de clientes registrados en el sistema
        self.clientes: list[Cliente] = []

    # --- Gestión de productos ---

    def agregar_producto(self, producto: Producto) -> None:
        """Añade un nuevo producto al catálogo del restaurante."""
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al menú.")

    def listar_productos(self) -> None:
        """Muestra todos los productos registrados en el sistema."""
        print(f"\n{'='*55}")
        print(f"  CATÁLOGO DE PRODUCTOS — {self.nombre}")
        print(f"{'='*55}")
        if not self.productos:
            print("  No hay productos registrados.")
        for producto in self.productos:
            print(f"  {producto}")
        print(f"{'='*55}\n")

    def listar_productos_disponibles(self) -> None:
        """Muestra únicamente los productos actualmente disponibles."""
        disponibles = [p for p in self.productos if p.disponible]
        print(f"\n{'='*55}")
        print(f"  MENÚ DISPONIBLE — {self.nombre}")
        print(f"{'='*55}")
        if not disponibles:
            print("  No hay productos disponibles en este momento.")
        for producto in disponibles:
            print(f"  {producto}")
        print(f"{'='*55}\n")

    # --- Gestión de clientes ---

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un nuevo cliente en el sistema."""
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado correctamente.")

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados en el sistema."""
        print(f"\n{'='*55}")
        print(f"  CLIENTES REGISTRADOS — {self.nombre}")
        print(f"{'='*55}")
        if not self.clientes:
            print("  No hay clientes registrados.")
        for cliente in self.clientes:
            print(f"  {cliente}")
        print(f"{'='*55}\n")

    def buscar_cliente_por_nombre(self, nombre: str) -> Cliente | None:
        """Busca y retorna un cliente por su nombre (sin distinción de mayúsculas)."""
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    def __str__(self) -> str:
        return (
            f"Restaurante: {self.nombre} "
            f"| Dirección: {self.direccion} "
            f"| Productos: {len(self.productos)} "
            f"| Clientes: {len(self.clientes)}"
        )
