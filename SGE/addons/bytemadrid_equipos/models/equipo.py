from odoo import models, fields


class Equipo (models.Model):
    _name = 'bytemadrid.equipo'
    _description = 'Equipo Informático'

    # Many2one enlaza con UN usuario interno existente (res.users).
    # domain restringe las opciones a usuarios que no sean de tipo portal/público.
    # ondelete='set null' evita eliminar el equipo si se elimina el usuario.
    proveedor_id= fields.Many2one(
        comodel_name = 'res.partner',
        string = 'Proveedor',
        ondelete = 'set null',
        help = 'Contacto de odoo que suministro este equipo.'
    )

    responsable_id= fields.Many2one(
        comodel_name= 'res.users',
        string = 'Responsable',
        domain = [('share', '=', False)],
        ondelete='set null',
        help='Usuario interno encargado del equipo.'
    )
    

    name = fields.Char(
        string="Nombre del equipo",
        required=True
    )

    fabricante = fields.Char(
        string="Nombre del fabricante",
        required=True
    )

    modelo = fields.Char(
        string="Nombre del modelo"
    )

    numero_serie = fields.Char(
        string="Número de serie"
    )

    precio = fields.Float(
        string="Precio"
    )

    activo = fields.Boolean(
        string="Activo",
        default=True
    )
