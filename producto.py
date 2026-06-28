# Clase que representa un producto disponible en el restaurante
# Puede ser un plato, bebida o postre del menú


class Producto:
    """Representa un ítem del menú del restaurante."""

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        calorias: int,
        disponible: bool
    ) -> None:
        # Nombre descriptivo del plato o bebida
        self.nombre: str = nombre
        # Categoría: "entrada", "plato fuerte", "postre", "bebida"
        self.categoria: str = categoria
        # Precio en dólares con decimales
        self.precio: float = precio
        # Calorías aproximadas del producto
        self.calorias: int = calorias
        # Indica si el producto está disponible en el menú actualmente
        self.disponible: bool = disponible

    def activar(self) -> None:
        """Marca el producto como disponible en el menú."""
        self.disponible = True

    def desactivar(self) -> None:
        """Retira el producto del menú temporalmente."""
        self.disponible = False

    def aplicar_descuento(self, porcentaje: float) -> float:
        """Calcula el precio con descuento sin modificar el precio original."""
        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"[{self.categoria.upper()}] {self.nombre} "
            f"| Precio: ${self.precio:.2f} "
            f"| Calorías: {self.calorias} kcal "
            f"| Estado: {estado}"
        )
