from django.shortcuts import redirect

class LoginSuperUsuarioMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(LoginSuperUsuarioMixin, self).dispatch(request, *args, **kwargs)
        return redirect('inicio')

class LoginProveedorUsuarioMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_proveedor:
            return super(LoginProveedorUsuarioMixin, self).dispatch(request, *args, **kwargs)
        return redirect('inicio')
