from django.contrib import admin
from libreta.models import Deuda, Desglose, HistorialPago
from linku.models import Cliente

class DesgloseInLine(admin.TabularInline):
    model = Desglose
    extra = 1

class HistorialPagoInLine(admin.TabularInline):
    model = HistorialPago
    extra = 1

class DeudaAdmin(admin.ModelAdmin):
    inlines = [DesgloseInLine, HistorialPagoInLine]
    readonly_fields = ('deudaActual',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "cliente" and not request.user.is_superuser:
            kwargs["queryset"] = Cliente.objects.filter(usuario=request.user)
        return super(DeudaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(DeudaAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.cliente.usuario.id:
            return False
        return True
    def queryset(self, request):
        if request.user.is_superuser:
            return Deuda.objects.all()
        return Deuda.objects.filter(cliente__usuario=request.user)


admin.site.register(Deuda, DeudaAdmin)
admin.site.register(Desglose)
admin.site.register(HistorialPago)
