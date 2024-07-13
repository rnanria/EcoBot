import random

def welcome():
    return "¡Hola! Bienvenido a EcoBot, tu guía para un futuro verde\n Soy un bot amigable creado para ayudarte a descubrir datos curiosos y emocionantes sobre nuestro planeta, además de proponerte retos sencillos pero significativos que puedes llevar a cabo en tu día a día para cuidar el medio ambiente.\n \n Si quieres saber los comandos disponible escribe: $comandos en el chat."
def dato_curioso():
    n = random.randint(1, 14)
    if n == 1:
        return "¡Adiós al plástico! Cada minuto se vende un millón de botellas de plástico en el mundo. El 42% del plástico que se utiliza termina en envases de un solo uso. Al reciclar una botella de plástico ahorramos la energía necesaria para mantener una bombilla encendida durante 6 horas."
    elif n == 2:
        return "El poder del aluminio: Reciclar una lata de aluminio ahorra la energía suficiente para ver la televisión durante 3 horas. ¡Y lo mejor es que el aluminio se puede reciclar infinitamente!"
    elif n == 3:
        return "Salvando árboles: Por cada tonelada de papel que se recicla, se salvan 17 árboles grandes. Además, la fabricación de papel reciclado consume un 62% menos de energía y un 86% menos de agua que la del papel nuevo."
    elif n == 4:
        return "¿Sabías que? Las 5  islas de basura más grandes del planeta ocupan una superficie 7 veces mayor que la de España. Si no cambiamos nuestros hábitos, en 2050 habrá más plástico que peces en los océanos."
    elif n == 5:
        return "Reutilizar, reducir y reciclar es la clave para la sostenibilidad. Evita el consumo innecesario, reutiliza todo lo que puedas y recicla correctamente los residuos que generes."
    elif n == 6:
        return "¿Sabías que las colillas tardan entre 12 y 15 años en biodegradarse?"
    elif n == 7:
        return "¿Sabías que? La producción de un solo par de jeans puede consumir hasta 2.700 litros de agua."
    elif n == 8:
        return "¿Sabías que? Las bolsas de plástico tardan entre 100 y 500 años en biodegradarse, mientras que las bolsas de tela solo unos meses."
    elif n == 9:
        return "¿Sabías que? El vidrio es 100% reciclable y se puede reutilizar una y otra vez."
    elif n == 10:
        return "¿Sabías que una pila de botón, la que usas en tu reloj, contamina hasta 600 mil litros de agua?"
    elif n == 11:
        return "¿Sabías que? Puedes llevar tus residuos electrónicos como: celulares, ordenadores, televisores. etc. A un punto de reciclaje especializado."
    elif n == 12:
        return "¿Sabías que compostar tus residuos de cocina y jardín puede reducir la cantidad de basura que envías al vertedero en hasta un 70%?"
    elif n == 13:
        return "¿Sabías que? puedes reducir envases comprando productos frescos en mercados locales o llevando tus propios recipientes a las tiendas."
    elif n == 14:
        return "¿Sabías que si todos los habitantes del planeta dejáramos de usar pajitas de plástico durante un año, ahorraríamos suficiente plástico como para llenar 100 ballenas azules?"
    else:
        return "¿Sabías que los productos de limpieza ecológicos están hechos con ingredientes naturales y biodegradables? esto significa que se descomponen naturalmente en el medio ambiente y no contaminan el agua ni el suelo."

def xp():
    p = random.randint(1,7)
    if p == 1:
        return "Apaga las luces y aparatos electrónicos que no estés usando. ¡Incluso un pequeño ahorro de energía marca la diferencia!"
    elif p == 2:
        return "Camina, usa bicicleta o transporte público cuando puedas. Si debes usar auto, comparte el viaje o elige un vehículo eco-amigable."
    elif p == 3:
        return "Lleva tu propia bolsa de tela, taza reutilizable y cubiertos para evitar el uso de plásticos de un solo uso."
    elif p == 4:
        return "Cierra la regadera mientras te enjabonas y reduce el tiempo que pasas bajo el agua."
    elif p == 5:
        return "Reduce el consumo de carne, compra productos locales y de temporada, y evita el desperdicio de alimentos."
    elif p == 6:
        return "Dale una nueva vida a la ropa que ya no usas y compra en tiendas de segunda mano."
    else:
        return "Cuando termines de cargar tus dispositivos electrónicos, desconecta los cargadores para evitar el consumo de energía fantasma."

def help():
    return "Comandos disponibles:\n • $hello: ¡Saluda conmigo y comienza tu aventura ecológica!\n • $dato: Descubre un dato curioso sobre el medio ambiente que te sorprenderá.\n • $reto: Acepta un reto sencillo y divertido para reducir tu huella de carbono.\n • $idea: Dime qué material deseas reciclar y te daré ideas creativas para reutilizarlo.\n ¡Explora y diviértete mientras aprendes a cuidar nuestro planeta!"
