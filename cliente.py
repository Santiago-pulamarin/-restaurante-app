# Clase que representa a un cliente registrado en el sistema del restaurante


class Cliente:
    """Representa a una persona registrada en el sistema del restaurante."""

    def __init__(
        self,
        nombre: str,
        correo: str,
        telefono: str,
        visitas: int,
        es_vip: bool
    ) -> None:
        # Nombre completo del cliente
        self.nombre: str = nombre
        # Correo electrónico para notificaciones y reservas
        self.correo: str = correo
        # Número de teléfono de contacto
        self.telefono: str = telefono
        # Cantidad de veces que el cliente ha visitado el restaurante
        self.visitas: int = visitas
        # Indica si el cliente tiene membresía VIP (beneficios especiales)
        self.es_vip: bool = es_vip

    def registrar_visita(self) -> None:
        """Incrementa el contador de visitas del cliente."""
        self.visitas += 1
        # Ascenso automático a VIP al alcanzar 10 visitas
        if self.visitas >= 10 and not self.es_vip:
            self.es_vip = True
            print(f"¡Felicitaciones, {self.nombre}! Ahora eres cliente VIP.")

    def obtener_descuento(self) -> float:
        """Retorna el porcentaje de descuento según el tipo de cliente."""
        if self.es_vip:
            return 15.0  # 15 % para clientes VIP
        return 5.0       # 5 % para clientes regulares

    def __str__(self) -> str:
        tipo = "VIP" if self.es_vip else "Regular"
        return (
            f"Cliente: {self.nombre} "
            f"| Correo: {self.correo} "
            f"| Tel: {self.telefono} "
            f"| Visitas: {self.visitas} "
            f"| Tipo: {tipo}"
        )
