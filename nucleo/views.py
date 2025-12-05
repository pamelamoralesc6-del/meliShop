from django.shortcuts import render, get_object_or_404,  redirect
from .models import Productos
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def registrar_producto(request):

    if request.method == "POST":

        Vtalla = request.POST['talla']
        Vcolor = request.POST['color']
        Vtipo_tela = request.POST['tipo_tela']
        Vprecio = request.POST['precio']
        Vdescripcion = request.POST['descripcion']
        Vstock = request.POST['stock']
        Vimagen_url = request.POST['imagen_url']

        producto_nuevo = Productos(
            talla = Vtalla,
            color = Vcolor,
            tipo_tela = Vtipo_tela,
            precio = Vprecio,
            descripcion = Vdescripcion,
            stock = Vstock,
            imagen_url = Vimagen_url
        )

        producto_nuevo.save()

        return render(request, "Registro.html",{
            "mensaje": "Producto Registrado Correctamente"
        })
    return render(request,'Registro.html')

def buscar_producto(request):
    resultado = []
    query = request.GET.get('consultar_producto')

    if query:
        resultado = Productos.objects.filter(
            Q(talla__icontains=query) | Q(precio__icontains=query) | Q(tipo_tela__icontains=query)
        )
    return render(request, 'buscar_producto.html',{'resultado':resultado})

def editar_producto(request, producto_id):
    productos = get_object_or_404(Productos, id=producto_id)

    if request.method == "POST":
        productos.talla = request.POST.get('talla',productos.talla)
        productos.color = request.POST.get('color',productos.color)
        productos.tipo_tela = request.POST.get('tipo_tela', productos.tipo_tela)
        productos.precio = request.POST.get('precio', productos.precio)
        productos.descripcion = request.POST.get('descripcion', productos.descripcion)
        productos.stock = request.POST.get('stock', productos.stock)
        productos.imagen_url = request.POST.get('imagen_url', productos.imagen_url)
        productos.save()
        return redirect('buscar_producto')
     
    return render(request,'editar_producto.html',{'produtos': productos})

def eliminar_producto(request, producto_id):
    producto_a_borrar = get_object_or_404(Productos, id=producto_id)

    if request.method == 'POST':
        producto_a_borrar.delete()
        return redirect('buscar_producto')
    return render(request, 'eliminar_producto.html',{'producto': producto_a_borrar})

