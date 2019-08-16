class ReadOnlyAdminMixin:
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ customize add/edit form to remove save / save and continue """
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super().change_view(request, object_id, extra_context=extra_context)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        fields = [field.name for field in obj._meta.fields]
        many_to_many = [field.name for field in obj._meta.many_to_many]
        return list(self.readonly_fields) + fields + many_to_many

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
