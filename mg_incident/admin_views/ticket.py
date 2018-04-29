from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from sqlalchemy.sql.functions import current_user
from wtforms import ValidationError

from mg_incident import db, admin
from mg_incident.auth import UserRequiredMixin
from mg_incident.models import Ticket, TicketStatus
from mg_incident.admin_views import formatters


class TicketView(UserRequiredMixin, ModelView):
    column_list = ['id', 'name', 'from_ticket', 'assigned_to',
                   'assigned_by', 'created_by', 'created_at', 'updated_at', ]
    column_filters = [
        'from_ticket.name',
        'from_ticket.id',
        'created_by.username',
        'assigned_by.username',
        'assigned_to.username',
    ]
    form_columns = ['name', 'description', 'assigned_to', 'from_ticket', ]
    column_type_formatters = formatters.DEFAULT_FORMATTERS
    can_view_details = True
    can_delete = True

    def on_model_delete(self, model):
        if model.chained_tickets:
            raise ValidationError("You can't deleting tickets that have child records")
    
    def on_model_change(self, form, model, is_created):
        from flask_security import current_user
        if is_created:
            model.created_by = current_user
        if not model.assigned_to == form.assigned_to:
            model.assigned_by = current_user


class TicketStatusView(UserRequiredMixin, ModelView):
    column_list = ['name', 'description', ]
    column_searchable_list = ['name', 'description', ]
    form_columns = ['name', 'description', ]
    can_view_details = True
    can_delete = True

    def on_model_delete(self, model):
        if model.is_predefined:
            raise ValidationError('Predefined status can not be deleted.')

    def on_model_change(self, form, model, is_created):
        if model.is_predefined and not is_created:
            raise ValidationError('Predefined status can not be changed.')


# class TicketStatusTrackingView(UserRequiredMixin, ModelView):
#     form_columns = ('ticket', 'ticket_status', 'description', 'created_by', 'created_at',)
#     column_filters = ('ticket.name', 'ticket_status.name', 'description', 'created_by.username',)
#     column_searchable_list = ('ticket.id', 'ticket_status.name', 'description',)
#     form_columns = ('ticket', 'ticket_status', 'description', 'created_by', 'created_at')


admin.add_views(
    TicketView(Ticket, db.session),
    TicketStatusView(TicketStatus, db.session),
)
