from django.contrib import admin
from linku.models import Cliente, Telefono, GrupoCliente

class TelefonoInline(admin.TabularInline):
    model = Telefono

class AdminCleinte(admin.ModelAdmin):
    exclude = ('usuario',)
    list_display = ('nombre', 'correo', 'usuario')
    search_fields=('id', 'nombre', 'correo','direccion', 'descripcion')
    inlines = [TelefonoInline,]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(AdminCleinte, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.usuario.id:
            return False
        return True
    def queryset(self, request):
        if request.user.is_superuser:
            return Cliente.objects.all()
        return Cliente.objects.filter(usuario=request.user)

class GrupoClienteAdmin(admin.ModelAdmin):
    filter_horizontal =('cliente',)
    exclude = ('usuario',)
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "cliente" and not request.user.is_superuser:
            kwargs["queryset"] = Cliente.objects.filter(usuario=request.user)
        return super(GrupoClienteAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(GrupoClienteAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.usuario.id:
            return False
        return True
    def queryset(self, request):
        if request.user.is_superuser:
            return GrupoCliente.objects.all()
        return GrupoCliente.objects.filter(usuario=request.user)

class TelefonoAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "cliente" and not request.user.is_superuser:
            kwargs["queryset"] = Cliente.objects.filter(usuario=request.user)
        return super(TelefonoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(TelefonoAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.cliente.usuario.id:
            return False
        return True
    def queryset(self, request):
        if request.user.is_superuser:
            return Telefono.objects.all()
        return Telefono.objects.filter(cliente__usuario=request.user)

admin.site.register(Cliente, AdminCleinte)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(GrupoCliente, GrupoClienteAdmin)