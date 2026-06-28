# Punto de arranque del sistema de gestión del restaurante
# Aquí se crean los objetos y se registran en el servicio principal

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    # --- Crear el restaurante ---
    mi_restaurante = Restaurante(
        nombre="La Mesa Feliz",
        direccion="Av. Amazonas 345, Quito"
    )
    print(f"\nSistema iniciado para: {mi_restaurante.nombre}\n")

    # --- Crear productos del menú ---
    sopa_del_dia = Producto(
        nombre="Sopa del día",
        categoria="entrada",
        precio=3.50,
        calorias=180,
        disponible=True
    )

    lomo_saltado = Producto(
        nombre="Lomo saltado",
        categoria="plato fuerte",
        precio=8.75,
        calorias=620,
        disponible=True
    )

    tiramisu = Producto(
        nombre="Tiramisú casero",
        categoria="postre",
        precio=4.25,
        calorias=310,
        disponible=False  # Temporalmente agotado
    )

    limonada_natural = Producto(
        nombre="Limonada natural",
        categoria="bebida",
        precio=2.00,
        calorias=95,
        disponible=True
    )

    # --- Registrar productos en el restaurante ---
    mi_restaurante.agregar_producto(sopa_del_dia)
    mi_restaurante.agregar_producto(lomo_saltado)
    mi_restaurante.agregar_producto(tiramisu)
    mi_restaurante.agregar_producto(limonada_natural)

    # --- Crear clientes ---
    cliente_ana = Cliente(
        nombre="Ana Torres",
        correo="ana.torres@email.com",
        telefono="0991234567",
        visitas=12,
        es_vip=True
    )

    cliente_luis = Cliente(
        nombre="Luis Paredes",
        correo="luis.paredes@email.com",
        telefono="0987654321",
        visitas=3,
        es_vip=False
    )

    cliente_maria = Cliente(
        nombre="María Salazar",
        correo="maria.salazar@email.com",
        telefono="0976543210",
        visitas=9,
        es_vip=False
    )

    # --- Registrar clientes en el restaurante ---
    mi_restaurante.registrar_cliente(cliente_ana)
    mi_restaurante.registrar_cliente(cliente_luis)
    mi_restaurante.registrar_cliente(cliente_maria)

    # --- Mostrar catálogo completo de productos ---
    mi_restaurante.listar_productos()

    # --- Mostrar solo productos disponibles ---
    mi_restaurante.listar_productos_disponibles()

    # --- Mostrar clientes registrados ---
    mi_restaurante.listar_clientes()

    # --- Demostrar uso de métodos adicionales ---
    print("=== ACCIONES DEL SISTEMA ===\n")

    # Registrar una nueva visita para Luis (lleva 3 → 4)
    cliente_luis.registrar_visita()
    print(f"  Visitas de {cliente_luis.nombre}: {cliente_luis.visitas}")

    # Consultar el descuento de cada cliente
    print(f"  Descuento de {cliente_ana.nombre}: {cliente_ana.obtener_descuento()}%")
    print(f"  Descuento de {cliente_luis.nombre}: {cliente_luis.obtener_descuento()}%")

    # Simular que María llega a 10 visitas y se convierte en VIP
    print()
    for _ in range(1):  # Solo le falta 1 visita para llegar a 10
        cliente_maria.registrar_visita()
    print(f"  Visitas de {cliente_maria.nombre}: {cliente_maria.visitas}")
    print(f"  ¿Es VIP {cliente_maria.nombre}? {cliente_maria.es_vip}")

    # Mostrar precio del lomo saltado con descuento VIP (15 %)
    precio_con_descuento = lomo_saltado.aplicar_descuento(15)
    print(f"\n  Precio de '{lomo_saltado.nombre}' con descuento VIP: ${precio_con_descuento}")

    # Activar el tiramisú (reingresa al menú)
    tiramisu.activar()
    print(f"\n  '{tiramisu.nombre}' activado: {tiramisu}")

    # Buscar un cliente por nombre
    print()
    encontrado = mi_restaurante.buscar_cliente_por_nombre("Luis Paredes")
    if encontrado:
        print(f"  Cliente encontrado → {encontrado}")

    # Resumen general del restaurante
    print(f"\n{'='*55}")
    print(f"  RESUMEN FINAL")
    print(f"{'='*55}")
    print(f"  {mi_restaurante}")
    print(f"{'='*55}\n")


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()
